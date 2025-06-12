from sqlalchemy import Column, String, Text, DateTime
from ..core.database import Base
from datetime import datetime
import uuid


class PromptModel(Base):
    __tablename__ = "prompts"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True)