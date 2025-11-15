from fastapi import APIRouter
from .schemas import EventSchemas

router = APIRouter()

# /api/router
@router.get("")
def read_events():
    return {"items": [1,2,3]}

@router.get("/{event_id}")
# -> EventSchemas, indique que la fonction est censé faire un retour d'un objet de type EventSchemas
def get_event(event_id:int) -> EventSchemas:
    return {"id": event_id}