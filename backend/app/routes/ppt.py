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
    """
        Handles the upload of a PowerPoint presentation file and verifies its integrity using a checksum.
        \n**Parameters**
        \n\tpresentation (UploadFile):
            The uploaded PowerPoint presentation file. It should be sent as a multipart/form-data file.
        \n\tchecksum (str):
            The SHA-256 checksum of the file content sent along with the file. This is used to validate the file's integrity.

        \n**Returns**
        \n\tDict[str, str]:
            A dictionary containing a success message and the filename where the presentation was saved.

        \n**Raises**
        \n\tHTTPException (400):
            Raised if the provided checksum does not match the computed checksum of the uploaded file.

        \n\tHTTPException (500):
            Raised for any unexpected errors during the processing or saving of the presentation.
    """
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
    """
        Processes a user's prompt for modifying a PowerPoint presentation based on contextual data and AI-generated suggestions.

        \n**Parameters**
            \n\trequest (Request):
                The HTTP request object containing JSON payload with the following expected structure:
                - slidesInfo (list): Information about slides, including index.
                - shapesInfo (optional, list): Information about shapes on the slide, including names.
                - attached_file (optional): Additional file attached by the user.

        \n**Returns**
            \n\tDict[str, Any]:
                A dictionary containing updated PowerPoint presentation details and the input data used for processing.

        \n**Raises**
            \n\tHTTPException (500):
                Raised if any unexpected error occurs during the processing.

        \n**Function Workflow**\n
            1. Parse Request Data:
               Extract and validate the JSON data from the incoming request.

            2. Retrieve Slide Context:
               - Create a `PresentationContext` object using the current PowerPoint file.
               - Retrieve the context for a specific slide and optionally a shape if provided.

            3. Prepare AI Prompt:
               - Select a prompt template based on whether shapes information is provided.
               - Generate user and system prompts using `PromptTemplate.generate_prompts`.

            4. Invoke GPT Service:
               - Use the GPT service to process the prompts and generate a response conforming to `ActionsList` schema.

            5. Handle PowerPoint Actions:
               - Instantiate a `PPTActionHandler` to process the GPT-generated actions.
               - Execute the actions and save the updated presentation.

            6. Return Response:
               - Return a dictionary containing the updated presentation details and the input data.
    """
    try:
        data = await request.json()

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
