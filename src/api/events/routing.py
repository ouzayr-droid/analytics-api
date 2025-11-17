# import os
from fastapi import APIRouter, Depends
from sqlmodel import Session
from .models import EventModel, EventListSchemas, EventCreateSchemas, EventUpdateSchemas
from api.db.session import get_session

router = APIRouter()
from api.db.config import DATABASE_URL

# /api/events
@router.get("/")
def read_events() -> EventListSchemas:
    print(DATABASE_URL)
    return {
        "results": [{"id":1},{"id":2},{"id":3}], 
        "count":3
    }

# POST /api/events
@router.post("/", response_model=EventModel)
def create_event(payload:EventCreateSchemas, session: Session = Depends(get_session)) -> EventModel:
    # a bunch of items in a table
    data = payload.model_dump() # payload -> dict -> pydantic
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

# GET /api/events/number
@router.get("/{event_id}")
# -> EventSchemas, indique que la fonction est censé faire un retour d'un objet de type EventSchemas
def get_event(event_id:int) -> EventModel:
    return {"id": event_id, "page": "str", "description": "x"}

# @router@get(event_id:int) -> EventModel:
    # a single
    # return {"id": event_id}