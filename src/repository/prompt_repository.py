from typing import List, Optional, Dict, Any
from datetime import datetime
import uuid
from ..model.prompt import PromptEntity, PromptCreateRequest, PromptUpdateRequest

class PromptRepository:
    """Repository para gerenciar prompts em memória (pode ser facilmente adaptado para banco de dados)"""
    
    def __init__(self):
        self._prompts: Dict[str, PromptEntity] = {}
    
    def create(self, prompt_data: PromptCreateRequest) -> PromptEntity:
        """Criar um novo prompt"""
        prompt_id = str(uuid.uuid4())
        now = datetime.utcnow()
        
        prompt_entity = PromptEntity(
            id=prompt_id,
            prompt=prompt_data.prompt,
            created_at=now
        )
        
        self._prompts[prompt_id] = prompt_entity
        return prompt_entity
    
    def get_by_id(self, prompt_id: str) -> Optional[PromptEntity]:
        """Buscar prompt por ID"""
        return self._prompts.get(prompt_id)
    
    def get_all(self, limit: int = 100, offset: int = 0) -> List[PromptEntity]:
        """Listar todos os prompts com paginação"""
        prompts = list(self._prompts.values())
        prompts.sort(key=lambda x: x.created_at, reverse=True)
        return prompts[offset:offset + limit]
    
    def update(self, prompt_id: str, update_data: PromptUpdateRequest) -> Optional[PromptEntity]:
        """Atualizar um prompt existente"""
        if prompt_id not in self._prompts:
            return None
        
        prompt = self._prompts[prompt_id]
        update_dict = update_data.dict(exclude_unset=True)
        
        if update_dict:
            for field, value in update_dict.items():
                setattr(prompt, field, value)
            prompt.updated_at = datetime.utcnow()
        
        return prompt
    
    def delete(self, prompt_id: str) -> bool:
        """Apagar um prompt"""
        if prompt_id in self._prompts:
            del self._prompts[prompt_id]
            return True
        return False
    
    def delete_all(self) -> int:
        """Apagar todos os prompts"""
        count = len(self._prompts)
        self._prompts.clear()
        return count
    
    def exists(self, prompt_id: str) -> bool:
        """Verificar se um prompt existe"""
        return prompt_id in self._prompts

# Instância singleton do repository
prompt_repository = PromptRepository() 