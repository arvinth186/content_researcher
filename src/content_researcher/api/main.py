from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
from src.content_researcher.api.runner import generate_article
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI(
    title="Content Researcher API",
    description="API for multi-agent content research and writing using CrewAI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResearchRequest(BaseModel):
    topic: str
    
@app.get("/")
def home():
    return {"message": "Welcome to the Content Researcher API! Use the /generate endpoint to create articles."}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/generate")
def research_topic(request: ResearchRequest):
    try:
        article = generate_article(request.topic)
        return {
            "topic": request.topic,
            "article": article
            }
    except Exception as e:
        return {"error": str(e)}
