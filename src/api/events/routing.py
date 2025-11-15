from fastapi import APIRouter
from .schemas import EventSchemas, EventListSchemas, EventCreateSchemas, EventUpdateSchemas

router = APIRouter()

# /api/events
@router.get("")
def read_events() -> EventListSchemas:
    return {
        "results": [{id:1},{id:2},{id:3}], 
        "count":3
    }

# GET /api/events/number
@router.get("/{event_id}")
# -> EventSchemas, indique que la fonction est censé faire un retour d'un objet de type EventSchemas
def get_event(event_id:int) -> EventSchemas:
    return {"id": event_id}

