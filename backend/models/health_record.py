from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    Date,
    ForeignKey
)
from sqlalchemy.orm import relationship

from database import Base


class HealthRecord(Base):
    __tablename__ = "health_records"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    steps = Column(Integer)

    water_intake_liters = Column(Float)

    sleep_hours = Column(Float)

    calories = Column(Integer)

    mood = Column(String(50))

    record_date = Column(Date)

    user = relationship(
        "User",
        back_populates="health_records"
    )