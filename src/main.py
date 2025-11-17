from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.db.session import init_db
from typing import Union
from api.events import router as event_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app start up
    init_db()
    yield
    # clean up

app = FastAPI(lifespan=lifespan)

# inclure la route importer à app
app.include_router(event_router, prefix="/api/events")

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q:Union[str, None]=None):
    return {"item_id": item_id, "q": q}

@app.get("/healthz")
def read_api_health():
    return {"status":"ok"}