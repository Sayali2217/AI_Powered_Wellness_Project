from fastapi import FastAPI

from database import Base, engine

from models.user import User
from models.user_profile import UserProfile
from models.health_record import HealthRecord
from models.productivity_log import ProductivityLog
from models.conversation import Conversation
from models.message import Message
from routes.auth import router as auth_router
from routes.profile import router as profile_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(profile_router)

app.include_router(auth_router)

@app.get("/health")
def health():
    return {"status": "Backend Running"}