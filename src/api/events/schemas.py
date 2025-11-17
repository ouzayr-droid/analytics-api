# design la manière dont les données seront présentées dans la logique métier
from pydantic import BaseModel, Field
from typing import List, Optional

class EventCreateSchemas(BaseModel):
    page: str
    description: Optional[str] = Field(default="")
    
class EventUpdateSchemas(BaseModel):
    description: str

class EventSchemas(BaseModel):
    id: int
    page: Optional[str] = ""
    description: Optional[str]=""

class EventListSchemas(BaseModel):
    results: List[EventSchemas]
    count: int