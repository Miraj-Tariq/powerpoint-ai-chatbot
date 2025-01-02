from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


# Define Enums for Actions and Icons
class ActionType(str, Enum):
    CREATE_TEXTBOX = "create_textbox"
    UPDATE_TEXTBOX = "update_textbox"
    CREATE_IMAGE = "create_image"
    UPDATE_IMAGE = "update_image"
    CREATE_ICON = "create_icon"
    UPDATE_ICON = "update_icon"
    DELETE_SHAPE = "delete_shape"


class IconType(str, Enum):
    BAR_CHART = "bar_chart"
    ENVIRONMENT = "environment"
    GEAR = "gear"
    GLOBE = "globe"
    ROBOT = "robot"
    TARGET = "target"


# Define Font Attributes
class FontAttributes(BaseModel):
    name: Optional[str] = Field(..., description="Font name")
    size: Optional[int] = Field(..., description="Font size")
    color: Optional[str] = Field(..., description="Font color in HEX format")
    bold: Optional[bool] = Field(..., description="Bold flag")
    italic: Optional[bool] = Field(..., description="Italic flag")
    underline: Optional[bool] = Field(..., description="Underline flag")


# Define Paragraph Attributes
class ParagraphAttributes(BaseModel):
    text: str = Field(..., description="Paragraph text")
    font: FontAttributes = Field(..., description="Font attributes")
    bullet: Optional[bool] = Field(..., description="Bullet point flag")
    level: Optional[int] = Field(..., description="Indentation level")


# Define Shape Parameters
class ShapeParameters(BaseModel):
    action_type: ActionType = Field(..., description="Action type")
    left: float = Field(..., description="Left position in millimeters")
    top: float = Field(..., description="Top position in millimeters")
    width: float = Field(..., description="Width in millimeters")
    height: float = Field(..., description="Height in millimeters")
    icon_name: Optional[IconType] = Field(..., description="Icon name for icon actions")
    word_wrap: Optional[bool] = Field(
        ...,
        description="Flag for word wrap property of the shape")
    paragraphs: Optional[List[ParagraphAttributes]] = Field(
        ...,
        description="List of paragraphs for text shapes")
    shape_name: Optional[str] = Field(..., description="Shape name")


# Define Actions List
class ActionsList(BaseModel):
    actions: List[ShapeParameters] = Field(
        ...,
        description="List of actions to perform")
