from fastapi import APIRouter, HTTPException, Request, UploadFile, File, Form

from app.config.settings import Settings
from app.constants import ICONS, POSSIBLE_ACTIONS, PROMPTS_MAP
from app.schemas.actions import ActionsList
from app.services.ppt.actions import PPTActionsService, PPTActionHandler
from app.services.ppt.context import PresentationContext
from app.utils.prompt import PromptTemplate

router = APIRouter()


@router.post("/upload")
async def upload_presentation(
        presentation: UploadFile = File(...),
        checksum: str = Form(...)):
    try:
        return PPTActionsService.save_ppt(presentation, checksum)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error saving presentation: {str(e)}"
        )


@router.post("/process")
async def process_user_prompt(request: Request):
    try:
        data = await request.json()
        print(f"INPUT DATA: {data}")

        # PPT CONTEXT
        presentation_context = PresentationContext(Settings.CURRENT_PPT)
        slide_context = presentation_context.get_slide_context(
            data["slidesInfo"][0]["index"],
            data["shapesInfo"][0]["name"] if "shapesInfo" in data
                                             and len(data["shapesInfo"]) else None
        )

        # PROMPT PREPARATION
        if "shapesInfo" in data and len(data["shapesInfo"]):
            selected_prompt_key = "actions_update"
        else:
            selected_prompt_key = "actions"
        prompt_template = PromptTemplate(
            PROMPTS_MAP,
            ICONS,
            POSSIBLE_ACTIONS
        )
        user_prompt, system_prompt = prompt_template.generate_prompts(
            prompt_key=selected_prompt_key,
            request_data=data,
            context_data=slide_context,
            covered_areas=slide_context["covered_areas"]
        )

        # RUN CHATGPT
        GPT_response = Settings.GPT_SERVICE.run_chatGPT(
            gpt_client=Settings.GPT_CLIENT,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            output_schema=ActionsList
        )
        # PERFORM GPT PROPOSED PPT ACTIONS
        ppt_action_handler = PPTActionHandler(
            Settings.CURRENT_PPT,
            presentation_context.slide_context.presentation,
            presentation_context.slide_context.get_slide(
                data["slidesInfo"][0]["index"]),
            data["slidesInfo"][0]["index"],
            GPT_response,
            slide_context["selected_shape"]["actual"]
            if "actual" in slide_context["selected_shape"] else None,
            data["attached_file"] if "attached_file" in data else None,
        )
        ppt_action_handler.execute_actions()
        updated_ppt_response = ppt_action_handler.save_presentation()
        updated_ppt_response["input_data"] = data

        return updated_ppt_response
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing user prompt: {str(e)}"
        )
