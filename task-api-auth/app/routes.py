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
        create_user(user.email, user.password)
        
        return{
            "message: User created successfully"
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail="Unable to create account. Please check your email and try again."
        )
        
    
@router.post("/login")
def login(user: UserLogin):
    try:
       response = authenticate_user(
           user.email,
           user.password
       )
       return{
           "message": "Login successful",
           "access_token": response.session.access_token,
           "token_type": "Bearer"
       }
       
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail="Invalid email or password."
        )
    

@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "role": current_user.role
    }