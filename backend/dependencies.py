from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from database import SessionLocal
from models.user import User
from utils.jwt import verify_access_token

security = HTTPBearer()


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    payload = verify_access_token(credentials.credentials)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user_id = int(payload["sub"])

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

