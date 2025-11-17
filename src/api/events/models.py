from typing import List, Optional
from sqlmodel import SQLModel, Field

class EventModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # id: int
    page: Optional[str] = ""
    description: Optional[str]=""

class EventCreateSchemas(SQLModel):
    page: str
    description: Optional[str] = Field(default="")
    
class EventUpdateSchemas(SQLModel):
    description: str

class EventListSchemas(SQLModel):
    results: List[EventModel]
    count: int