from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings
from app.db.session import engine, Base
from app.models.models import User , Recipient


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Gift Recommendation System",
    version="1.0.0"
)

@app.on_event("startup")
async def startup():
  async with engine.begin()as conn:
    await conn.run_sync(Base.metadata.create_all)

app.include_router(api_router,prefix = "/api/v1")

@app.get("/")
async def root():
  return{
    "status" : "online" , 
    "message": "GiftAI is working...",
    "docs": "/docs"
  }
