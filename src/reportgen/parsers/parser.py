from pydantic import BaseModel,Field
from typing import List

class Section(BaseModel):
    name: str = Field(description="the title of the section for the report ")
    description: str =Field(description=" overview about the main topics and concepts that should be written in this section of the report")

class list_sections(BaseModel):
    sections : List[Section] =Field("sections of the report")