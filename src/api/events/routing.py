# import os
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from .models import EventModel, EventListSchemas, EventCreateSchemas, EventUpdateSchemas
from api.db.session import get_session

router = APIRouter()
from api.db.config import DATABASE_URL

# /api/events
@router.get("/", response_model=EventListSchemas)
def read_events(session: Session = Depends(get_session)):
    query = select(EventModel).order_by(EventModel.id.desc()) #.limit(10)
    results = session.exec(query).all()
    return {
        "results": results, 
        "count": len(results)
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
@router.get("/{event_id}", response_model=EventModel)
# -> EventSchemas, indique que la fonction est censé faire un retour d'un objet de type EventSchemas
def get_event(event_id:int, session: Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()
    if not result:
        raise HTTPException(status_code=404, detail="Event not found !")
    return result

# @router@get(event_id:int) -> EventModel:
    # a single
    # return {"id": event_id}