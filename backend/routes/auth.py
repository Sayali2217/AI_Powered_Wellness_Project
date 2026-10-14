from fastapi import APIRouter 
from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from utils.jwt import verify_access_token

from schemas.auth import LoginRequest, Token
from utils.security import verify_password
from utils.jwt import create_access_token

from sqlalchemy.orm import Session

from schemas.user import UserRegister

from models.user import User

from dependencies import get_db

from utils.security import hash_password

from dependencies import get_current_user
router = APIRouter()

security = HTTPBearer()

@router.get("/me")
def me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }
    return current_user
@router.post("/login", response_model=Token) #response model is Token cause 
def login(
    user: LoginRequest,
    db: Session = Depends(get_db),
):

    db_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if not db_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    if not verify_password(
        user.password,
        db_user.password_hash,
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        {
            "sub": str(db_user.id)
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }

@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=hash_password(
            user.password
        )
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }