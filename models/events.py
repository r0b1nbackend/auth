from sqlmodel import SQLModel,JSON,Field,Column
from typing import List,Optional


class Event(SQLModel,table=True):
    id:int = Field(default=None,primary_key=True)
    title:str
    image:str
    description:str
    tags:List[str] = Field(as_column = JSON)
    location:str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example":{
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book","launch"],
                "location": "Google Meet"
            }
        }


class EventUpdate(SQLModel):
    title:str
    image:str
    description:str
    tags:List[str]
    location:str

    class Config:
        schema_extra = {
            "example":{
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }