from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

class PromptEntity(BaseModel):
    id: str
    prompt: str
    response: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class PromptCreateRequest(BaseModel):
    prompt: str
    
    @validator('prompt')
    def prompt_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError('O prompt não pode ser vazio.')
        return value

class PromptUpdateRequest(BaseModel):
    prompt: Optional[str] = None
    response: Optional[str] = None

class PromptResponse(BaseModel):
    id: str
    prompt: str
    response: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
