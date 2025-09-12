import uuid
from datetime import datetime
from typing import List, Optional

from sqlalchemy.orm import Session

from src.core.db import get_db
from src.models.prompt_model import PromptModel
from src.schemas.prompt_schema import (
    PromptCreateRequest,
    PromptEntity,
    PromptUpdateRequest,
)


class PromptQueries:
    
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, prompt_data: PromptCreateRequest) -> PromptEntity:
        prompt_id = str(uuid.uuid4())
        now = datetime.utcnow()
        
        db_prompt = PromptModel(
            id=prompt_id,
            prompt=prompt_data.prompt,
            created_at=now
        )
        
        self.db.add(db_prompt)
        self.db.commit()
        self.db.refresh(db_prompt)
        
        return PromptEntity(
            id=db_prompt.id,
            prompt=db_prompt.prompt,
            response=db_prompt.response,
            created_at=db_prompt.created_at,
            updated_at=db_prompt.updated_at
        )
    
    def get_by_id(self, prompt_id: str) -> Optional[PromptEntity]:
        db_prompt = self.db.query(PromptModel).filter(PromptModel.id == prompt_id).first()
        
        if db_prompt:
            return PromptEntity(
                id=db_prompt.id,
                prompt=db_prompt.prompt,
                response=db_prompt.response,
                created_at=db_prompt.created_at,
                updated_at=db_prompt.updated_at
            )
        return None
    
    def get_all(self, limit: int = 100, offset: int = 0) -> List[PromptEntity]:
        db_prompts = self.db.query(PromptModel).order_by(PromptModel.created_at.desc()).limit(limit).offset(offset).all()
        
        return [
            PromptEntity(
                id=prompt.id,
                prompt=prompt.prompt,
                response=prompt.response,
                created_at=prompt.created_at,
                updated_at=prompt.updated_at
            )
            for prompt in db_prompts
        ]
    
    def update(self, prompt_id: str, update_data: PromptUpdateRequest) -> Optional[PromptEntity]:
        update_dict = update_data.model_dump(exclude_unset=True)
        
        if update_dict:
            update_dict['updated_at'] = datetime.utcnow()
            self.db.query(PromptModel).filter(PromptModel.id == prompt_id).update(update_dict)
            self.db.commit()
        
        return self.get_by_id(prompt_id)
    
    def delete(self, prompt_id: str) -> bool:
        result = self.db.query(PromptModel).filter(PromptModel.id == prompt_id).delete()
        self.db.commit()
        return result > 0

    def delete_all(self) -> int:
        result = self.db.query(PromptModel).delete()
        self.db.commit()
        return result
    
    def exists(self, prompt_id: str) -> bool:
        return self.db.query(PromptModel).filter(PromptModel.id == prompt_id).first() is not None

prompt_repository = PromptQueries(db=next(get_db())) 