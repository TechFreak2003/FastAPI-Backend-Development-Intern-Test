from fastapi import APIRouter, HTTPException, status
from models import LoginRequest, LoginResponse, ErrorResponse
from auth import authenticate_user

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    """User login endpoint"""
    token = authenticate_user(request.username, request.password)
    
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    
    return LoginResponse(token=token)