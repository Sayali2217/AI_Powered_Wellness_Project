from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models.user import User
from models.user_profile import UserProfile
from schemas.profile import ProfileCreate
from dependencies import get_current_user

router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_profile(
    profile: ProfileCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    existing_profile = db.query(UserProfile).filter(
        UserProfile.user_id == current_user.id
    ).first()

    if existing_profile:

        raise HTTPException(
            status_code=400,
            detail="Profile already exists"
        )

    new_profile = UserProfile(
        user_id=current_user.id,
        age=profile.age,
        height=profile.height,
        weight=profile.weight,
        fitness_goal=profile.fitness_goal,
        diet_preference=profile.diet_preference,
        sleep_goal=profile.sleep_goal,
        water_goal=profile.water_goal
    )

    db.add(new_profile)

    db.commit()

    db.refresh(new_profile)

    return new_profile

@router.get("/")
def get_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    profile = db.query(UserProfile).filter(
        UserProfile.user_id == current_user.id
    ).first()

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    return profile

@router.put("/")
def update_profile(
    profile_data: ProfileCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    profile = db.query(UserProfile).filter(
        UserProfile.user_id == current_user.id
    ).first()

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    profile.age = profile_data.age
    profile.height = profile_data.height
    profile.weight = profile_data.weight
    profile.fitness_goal = profile_data.fitness_goal
    profile.diet_preference = profile_data.diet_preference
    profile.sleep_goal = profile_data.sleep_goal
    profile.water_goal = profile_data.water_goal

    db.commit()

    db.refresh(profile)

    return profile

@router.delete("/")
def delete_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    profile = db.query(UserProfile).filter(
        UserProfile.user_id == current_user.id
    ).first()

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    db.delete(profile)

    db.commit()

    return {
        "message": "Profile deleted successfully"
    }