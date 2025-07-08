from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import List
from models import HistoryItem
from auth import get_user_history, get_current_user
from routes.prompt_routes import get_current_user_from_token

router = APIRouter()

@router.get("/history", response_model=List[HistoryItem])
async def get_prompt_history(current_user: str = Depends(get_current_user_from_token)):
    """Get user's prompt history"""
    history = get_user_history(current_user)
    return history