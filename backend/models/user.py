from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(255), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=True)

    google_id = Column(String(255), nullable=True)

    is_email_verified = Column(Boolean, default=False)

    is_2fa_enabled = Column(Boolean, default=False)

    totp_secret = Column(String(255), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    profile = relationship(
        "UserProfile",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    health_records = relationship(
        "HealthRecord",
        back_populates="user"
    )

    productivity_logs = relationship(
        "ProductivityLog",
        back_populates="user"
    )

    conversations = relationship(
        "Conversation",
        back_populates="user"
    )