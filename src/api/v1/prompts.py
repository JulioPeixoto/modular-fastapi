from fastapi import APIRouter, HTTPException, Query, Depends
from typing import List

from ...model.prompt import PromptCreateRequest, PromptUpdateRequest, PromptResponse
from ...services.prompt_service import PromptService, get_prompt_service

router = APIRouter(tags=["prompts"])

@router.post("/prompts", response_model=PromptResponse, status_code=201)
def create_prompt(request: PromptCreateRequest, service: PromptService = Depends(get_prompt_service)):
    try:
        return service.create_prompt_with_response(request)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/prompts", response_model=List[PromptResponse])
def list_prompts(
    limit: int = Query(default=100, ge=1, le=1000),
    offset: int = Query(default=0, ge=0),
    service: PromptService = Depends(get_prompt_service)
):
    return service.list_prompts(limit=limit, offset=offset)

@router.get("/prompts/{prompt_id}", response_model=PromptResponse)
def get_prompt(prompt_id: str, service: PromptService = Depends(get_prompt_service)):
    prompt = service.get_prompt_by_id(prompt_id)
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt não encontrado")
    return prompt

@router.put("/prompts/{prompt_id}", response_model=PromptResponse)
def update_prompt(prompt_id: str, update_data: PromptUpdateRequest, service: PromptService = Depends(get_prompt_service)):
    updated_prompt = service.update_prompt(prompt_id, update_data)
    if not updated_prompt:
        raise HTTPException(status_code=404, detail="Prompt não encontrado")
    return updated_prompt

@router.delete("/prompts/{prompt_id}")
def delete_prompt(prompt_id: str, service: PromptService = Depends(get_prompt_service)):
    result = service.delete_prompt(prompt_id)
    if not result:
        raise HTTPException(status_code=404, detail="Prompt não encontrado")
    return {"message": "Prompt apagado com sucesso"}

@router.delete("/prompts")
def delete_all_prompts(service: PromptService = Depends(get_prompt_service)):
    count = service.delete_all_prompts()
    return {"message": f"{count} prompts apagados com sucesso"} 