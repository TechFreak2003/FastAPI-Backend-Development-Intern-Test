from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routes import auth_routes, prompt_routes, history_routes

# Create FastAPI app
app = FastAPI(
    title="Backend Development Intern Test",
    description="A simple FastAPI app with authentication and prompt handling",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_routes.router, tags=["Authentication"])
app.include_router(prompt_routes.router, tags=["Prompts"])
app.include_router(history_routes.router, tags=["History"])

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Backend Development Intern Test API"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)