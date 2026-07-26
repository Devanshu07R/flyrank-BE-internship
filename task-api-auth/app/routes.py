from fastapi import APIRouter
from app.schemas import UserSignup, UserLogin
from app.services import create_user, authenticate_user
from fastapi import Depends
from app.dependencies import get_current_user
from fastapi import HTTPException


router = APIRouter()


@router.post("/signup")
def signup(user: UserSignup):
    try:
        return create_user(user.email, user.password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(user: UserLogin):
    try:
        return authenticate_user(user.email, user.password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return current_user