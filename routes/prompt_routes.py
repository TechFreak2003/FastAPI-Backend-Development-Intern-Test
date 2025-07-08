import random
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models import PromptRequest, PromptResponse
from auth import get_current_user, add_prompt_to_history

router = APIRouter()
security = HTTPBearer()

# Fake AI responses
FAKE_RESPONSES = [
    "Interesting... Let's explore that idea.",
    "Let me think about that for a moment...",
    "That's a fascinating question!",
    "I see what you're getting at...",
    "Here's my take on that...",
    "Great question! Let me break it down...",
    "That reminds me of an interesting concept...",
    "I'd love to help you with that!",
    "That's worth considering from multiple angles...",
    "Let me process that information..."
]

def get_current_user_from_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Dependency to get current user from Bearer token"""
    try:
        # Get the token and clean it up
        token = credentials.credentials
        
        # Remove "Bearer " prefix if it exists (just in case)
        if token.startswith("Bearer "):
            token = token[7:]
        
        print(f"Cleaned token: {token}")  # Debug print
        username = get_current_user(token)
        print(f"Username from token: {username}")  # Debug print
        
        if not username:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        return username
    except Exception as e:
        print(f"Token validation error: {e}")  # Debug print
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

@router.post("/prompt", response_model=PromptResponse)
async def submit_prompt(
    request: PromptRequest, 
    current_user: str = Depends(get_current_user_from_token)
):
    """Submit a prompt and get a fake AI response"""
    # Generate a random fake response
    fake_response = random.choice(FAKE_RESPONSES)
    
    # Store in user's history
    add_prompt_to_history(current_user, request.prompt, fake_response)
    
    return PromptResponse(response=fake_response)