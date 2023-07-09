from fastapi import APIRouter,Body,HTTPException,status
from models.events import Event
from typing import List

event_router=APIRouter(
    tags=["Events"]
)

events=[]


@event_router.get("/",response_model=List[Event])
async def retrieve_all_events() -> Event:
    return events


@event_router.get("/{id}",response_model=Event)
async def retrieve_vent(id:int) -> Event:
    for event in events:
        if event.id == id:
            return events
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event wasn't found"
    )


@event_router.post("/new")
async def create_event(body:Event = Body(...)) -> dict:
    events.append(body)
    return {
        "message":"Event was created successfully"
    }


@event_router.delete("/")
async def delete_all_event() -> dict:
    events.clear()
    return {
        "message":"Events deleted successfully"
    }