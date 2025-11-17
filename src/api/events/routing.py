import os
from fastapi import APIRouter
from .models import EventModel, EventListSchemas, EventCreateSchemas, EventUpdateSchemas

router = APIRouter()
from api.db.config import DATABASE_URL

# /api/events
@router.get("/")
def read_events() -> EventListSchemas:
    print(os.environ.get("DATABASE_URL"), DATABASE_URL)
    return {
        "results": [{"id":1},{"id":2},{"id":3}], 
        "count":3
    }

# POST /api/events
@router.post("/")
def create_event(payload:EventCreateSchemas) -> EventModel:
    # a bunch of items in a table
    data = payload.model_dump() # payload -> dict -> pydantic
    return {"id":123, **data}

# GET /api/events/number
@router.get("/{event_id}")
# -> EventSchemas, indique que la fonction est censé faire un retour d'un objet de type EventSchemas
def get_event(event_id:int) -> EventSchemas:
    return {"id": event_id, "page": "str", "description": "x"}

