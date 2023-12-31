from pydantic import BaseModel,EmailStr
from typing import Optional,List
from models.events import Event


class User(BaseModel):
    email:EmailStr
    password:str

    class Config:
        schema_extra = {
            "example":{
                "email":"senkuchem1stry@gmail.com",
                "password":"2d3d4d5d",
            }
        }


class UserSignIn(BaseModel):
    email:EmailStr
    password:str

    class Config:
        schema_extra = {
            "example":{
                "email":"senkuchem1stry@gmail.com",
                "password":"2d3d4d5d",
            }
        }