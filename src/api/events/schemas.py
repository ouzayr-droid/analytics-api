# design la manière dont les données seront présentées dans la logique métier
from pydantic import BaseModel

class EventSchemas(BaseModel):
    id: int 