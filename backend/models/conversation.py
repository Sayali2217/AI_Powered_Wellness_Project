from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    title = Column(String(255))

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="conversations"
    )

    messages = relationship(
        "Message",
        back_populates="conversation"
    )