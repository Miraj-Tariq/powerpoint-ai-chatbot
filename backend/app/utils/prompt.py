from typing import Dict, Any, Tuple, List


class PromptTemplate:
    """
    Encapsulates the logic for building user and system prompts based on templates.
    """

    def __init__(self,
                 prompts_map: Dict[str, Dict[str, Any]],
                 icon_names: List[Dict[str, str]],
                 possible_actions: List[Dict[str, str]]):
        self.prompts_map = prompts_map
        self.icon_names = icon_names
        self.possible_actions = possible_actions

    def generate_prompts(self,
                         prompt_key: str,
                         request_data: Dict[str, Any],
                         context_data: Dict[str, Any],
                         covered_areas: List[Tuple[float, float, float, float]]
                         ) -> Tuple[str, str]:
        try:
            placeholders = set(self.prompts_map[prompt_key]["user"]
                               ["placeholders_list"])
            prompt_placeholders_data = self._prepare_placeholders(
                placeholders, request_data, context_data, covered_areas
            )

            user_prompt = (self.prompts_map[prompt_key]["user"]["prompt"].
                           format(**prompt_placeholders_data))
            system_prompt = (self.prompts_map[prompt_key]["system"]["prompt"].
                             format(**prompt_placeholders_data))

            return user_prompt, system_prompt

        except KeyError as e:
            raise ValueError(f"Missing required key in prompts_map: {str(e)}")

    def _prepare_placeholders(self,
                              placeholders: set,
                              request_data: Dict[str, Any],
                              context_data: Dict[str, Any],
                              covered_areas: List[Tuple[float, float, float, float]]
                              ) -> Dict[str, Any]:
        placeholder_data = {}

        if "covered_areas" in placeholders and covered_areas:
            placeholder_data["covered_areas"] = covered_areas
        if "icon_names" in placeholders:
            placeholder_data["icon_names"] = self.icon_names
        if "possible_actions" in placeholders:
            placeholder_data["possible_actions"] = self.possible_actions

        if request_data:
            if "user_instruction" in placeholders:
                placeholder_data["user_instruction"] = request_data.get("prompt", "")
            if "selected_shape_name" in placeholders:
                shape_info = request_data.get("shapesInfo", [])
                if shape_info:
                    placeholder_data["selected_shape_name"] = (
                        shape_info[0].get("name", ""))

        if context_data:
            self._add_context_data(placeholders, placeholder_data, context_data)

        return placeholder_data

    def _add_context_data(self,
                          placeholders: set,
                          placeholder_data: Dict[str, Any],
                          context_data: Dict[str, Any]) -> None:
        if "context_data" in placeholders:
            placeholder_data["context_data"] = context_data
        if "slide_width" in placeholders:
            placeholder_data["slide_width"] = (
                context_data)["presentation_info"]["slide_width"]
        if "slide_height" in placeholders:
            placeholder_data["slide_height"] = (
                context_data)["presentation_info"]["slide_height"]

        if context_data.get("selected_shape"):
            all_shapes = context_data["shapes"]
            shape_relative_idx = context_data["selected_shape"]["relative"]
            selected_shape_info = context_data["selected_shape"]["info"]

            if "shape_left" in placeholders:
                placeholder_data["shape_left"] = all_shapes[shape_relative_idx]["left"]
            if "shape_top" in placeholders:
                placeholder_data["shape_top"] = all_shapes[shape_relative_idx]["top"]
            if "shape_width" in placeholders:
                placeholder_data["shape_width"] = (
                    all_shapes)[shape_relative_idx]["width"]
            if "shape_height" in placeholders:
                placeholder_data["shape_height"] = (
                    all_shapes)[shape_relative_idx]["height"]
            if "shape_data" in placeholders:
                placeholder_data["shape_data"] = {
                    "shape_name": selected_shape_info["name"],
                    "shape_type": selected_shape_info["shape_type"],
                    "shape_left": selected_shape_info["left"],
                    "shape_top": selected_shape_info["top"],
                    "shape_width": selected_shape_info["width"],
                    "shape_height": selected_shape_info["height"],
                }
