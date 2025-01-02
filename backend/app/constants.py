from app.prompts import actions, actions_update

ICONS = [
    {"name": "bar_chart.png", "description": "Bar Chart"},
    {"name": "environment.png", "description": "Environment Friendly"},
    {"name": "gear.png", "description": "Mechanical Gear"},
    {"name": "globe.png", "description": "Globe"},
    {"name": "robot.png", "description": "Robot"},
    {"name": "target.png", "description": "Arrow hitting target"},
]

POSSIBLE_ACTIONS = [
    {
        "name": "create_textbox",
        "model_name": "CreateTextBoxParameters",
        "description": "Create Textbox"
    },
    {
        "name": "create_image",
        "model_name": "CreateImageParameters",
        "description": "Create Image"
    },
    {
        "name": "create_icon",
        "model_name": "CreateIconParameters",
        "description": "Create Icon"
    },
]

PROMPTS_MAP = {
    "actions": {
        "system": {
            "placeholders_list": [],
            "prompt": actions.actions_system_prompt,
        },
        "user": {
            "placeholders_list": [
                "user_instruction",
                "context_data",
                "covered_areas",
                "selected_shape_name",
                "slide_width",
                "slide_height",
                "icon_names",
                "possible_actions"
            ],
            "prompt": actions.actions_user_prompt,
        }
    },
    "actions_update": {
        "system": {
            "placeholders_list": [],
            "prompt": actions_update.actions_update_system_prompt,
        },
        "user": {
            "placeholders_list": [
                "user_instruction",
                "context_data",
                "shape_data",
                "covered_areas",
                "selected_shape_name",
                "slide_width",
                "slide_height",
                "icon_names",
                "possible_actions"
            ],
            "prompt": actions_update.actions_update_user_prompt,
        }
    },
}
