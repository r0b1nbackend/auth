from fastapi import APIRouter,HTTPException,status
from models.users import User,UserSignIn,NewUser


user_router = APIRouter(
    tags=["User"]
)

users = {}


@user_router.post("/signup")
async def sign_new_user(data:NewUser) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied ID exists"
        )
    users[data.email] = data
    return {
        "message":"User successfully registered"
    }


@user_router.post("/signin")
async def sign_user_in(user:UserSignIn) -> dict:
    if users[user.email] not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wrong credentials passed"
        )
    return {
        "message":"User signed in successfully"
    }