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


class ProductivityLog(Base):
    __tablename__ = "productivity_logs"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    focus_hours = Column(Float)

    tasks_completed = Column(Integer)

    journal = Column(String(1000))

    record_date = Column(Date)

    user = relationship(
        "User",
        back_populates="productivity_logs"
    )