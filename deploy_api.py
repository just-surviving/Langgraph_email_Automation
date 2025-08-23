import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes
from src.graph import Workflow
from dotenv import load_dotenv

# Load .env file
load_dotenv()


app = FastAPI(
    title="Gmail Automation",
    version="1.0",
    description="LangGraph backend for the AI Gmail automation workflow",
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

def get_runnable():
    return  Workflow().app

# Fetch LangGraph Automation runnable which generates the workouts
runnable = get_runnable()

# Create the Fast API route to invoke the runnable
add_routes(app, runnable)

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy", "service": "LangGraph Email Agent"}

def main():
    # Start the API
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()# API deployment ready: 2025-08-19
# API deployment ready: 2025-08-19
