from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.db import get_db
from src.db.repository.prompt_repository import PromptQueries
from src.domain.schemas.prompt_schema import (
    PromptCreateRequest,
    PromptResponse,
    PromptUpdateRequest,
)


class PromptService:

    def __init__(self, repository: PromptQueries):
        self.repository = repository

    def create_prompt_with_response(
        self, request: PromptCreateRequest
    ) -> PromptResponse:
        try:
            prompt_entity = self.repository.create(request)
            ai_response = "mock response"
            update_data = PromptUpdateRequest(response=ai_response)
            updated_prompt = self.repository.update(prompt_entity.id, update_data)

            if updated_prompt:
                return PromptResponse(**updated_prompt.model_dump())
            else:
                return PromptResponse(**prompt_entity.model_dump())

        except Exception as e:
            if 'prompt_entity' in locals() and prompt_entity:
                return PromptResponse(**prompt_entity.model_dump())
            raise e

    def get_prompt_by_id(self, prompt_id: str) -> Optional[PromptResponse]:
        prompt = self.repository.get_by_id(prompt_id)
        if prompt:
            return PromptResponse(**prompt.model_dump())
        return None

    def list_prompts(self, limit: int = 100, offset: int = 0) -> List[PromptResponse]:
        prompts = self.repository.get_all(limit=limit, offset=offset)
        return [PromptResponse(**prompt.model_dump()) for prompt in prompts]

    def update_prompt(
        self, prompt_id: str, update_data: PromptUpdateRequest
    ) -> Optional[PromptResponse]:
        if not self.repository.get_by_id(prompt_id):
            return None

        updated_prompt = self.repository.update(prompt_id, update_data)
        if updated_prompt is not None:
            return PromptResponse(**updated_prompt.model_dump())
        return None

    def delete_prompt(self, prompt_id: str) -> bool:
        return self.repository.delete(prompt_id)

    def delete_all_prompts(self) -> int:
        return self.repository.delete_all()

    def prompt_exists(self, prompt_id: str) -> bool:
        return self.repository.exists(prompt_id)


def get_prompt_service(db: Session = Depends(get_db)) -> PromptService:
    queries = PromptQueries(db)
    return PromptService(queries)
