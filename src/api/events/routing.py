from fastapi import APIRouter

router = APIRouter()

# /api/router
@router.get("/api/events")
def read_events():
    return {"items": [1,2,3]}