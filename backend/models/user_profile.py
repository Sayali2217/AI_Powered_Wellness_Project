from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class UserProfile(Base):

    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    age = Column(Integer, nullable=True)

    height = Column(Float, nullable=True)

    weight = Column(Float, nullable=True)

    fitness_goal = Column(String(100), nullable=True)

    diet_preference = Column(String(100), nullable=True)

    sleep_goal = Column(Float, nullable=True)

    water_goal = Column(Float, nullable=True)

    user = relationship(
        "User",
        back_populates="profile"
    )