from typing import List, Optional
from ..model.prompt import (
    PromptEntity, 
    PromptCreateRequest, 
    PromptUpdateRequest, 
    PromptResponse
)
from ..repository.prompt_repository import prompt_repository
from ..lib import chains

class PromptService:
    """Service para gerenciar a lógica de negócio dos prompts"""
    
    def __init__(self, repository=prompt_repository):
        self.repository = repository
    
    async def create_prompt_with_response(self, request: PromptCreateRequest) -> PromptResponse:
        """
        Criar um novo prompt, processar com IA e salvar no banco de dados
        """
        try:
            # 1. Criar o prompt no repositório
            prompt_entity = self.repository.create(request)
            
            # 2. Processar o prompt com a IA
            ai_response = chains.openai_request(request.prompt)
            
            # 3. Atualizar o prompt com a resposta da IA
            update_data = PromptUpdateRequest(response=ai_response)
            updated_prompt = self.repository.update(prompt_entity.id, update_data)
            
            # 4. Retornar a resposta formatada
            return PromptResponse(**updated_prompt.dict())
            
        except Exception as e:
            # Se der erro na IA, ainda assim salva o prompt
            if 'prompt_entity' in locals():
                return PromptResponse(**prompt_entity.dict())
            raise e
    
    def get_prompt_by_id(self, prompt_id: str) -> Optional[PromptResponse]:
        """Buscar um prompt específico por ID"""
        prompt = self.repository.get_by_id(prompt_id)
        if prompt:
            return PromptResponse(**prompt.dict())
        return None
    
    def list_prompts(self, limit: int = 100, offset: int = 0) -> List[PromptResponse]:
        """Listar todos os prompts com paginação"""
        prompts = self.repository.get_all(limit=limit, offset=offset)
        return [PromptResponse(**prompt.dict()) for prompt in prompts]
    
    def update_prompt(self, prompt_id: str, update_data: PromptUpdateRequest) -> Optional[PromptResponse]:
        """Atualizar um prompt existente"""
        if not self.repository.exists(prompt_id):
            return None
        
        updated_prompt = self.repository.update(prompt_id, update_data)
        if updated_prompt:
            return PromptResponse(**updated_prompt.dict())
        return None
    
    def delete_prompt(self, prompt_id: str) -> bool:
        """Apagar um prompt específico"""
        return self.repository.delete(prompt_id)
    
    def delete_all_prompts(self) -> int:
        """Apagar todos os prompts"""
        return self.repository.delete_all()
    
    def prompt_exists(self, prompt_id: str) -> bool:
        """Verificar se um prompt existe"""
        return self.repository.exists(prompt_id)

# Instância singleton do service
prompt_service = PromptService()
