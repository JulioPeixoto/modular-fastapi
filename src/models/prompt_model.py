import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, String, Text

from ..core.db import Base


class PromptModel(Base):
    __tablename__ = "prompts"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True)
