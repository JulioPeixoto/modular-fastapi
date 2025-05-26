from fastapi import APIRouter, HTTPException, Query
from typing import List

from ...model.prompt import PromptCreateRequest, PromptUpdateRequest, PromptResponse
from ...services.prompt_service import prompt_service

router = APIRouter(tags=["prompts"])

@router.post("/prompts", response_model=PromptResponse, status_code=201)
async def create_prompt(request: PromptCreateRequest):
    try:
        return await prompt_service.create_prompt_with_response(request)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/prompts", response_model=List[PromptResponse])
async def list_prompts(
    limit: int = Query(default=100, ge=1, le=1000),
    offset: int = Query(default=0, ge=0)
):
    return prompt_service.list_prompts(limit=limit, offset=offset)

@router.get("/prompts/{prompt_id}", response_model=PromptResponse)
async def get_prompt(prompt_id: str):
    prompt = prompt_service.get_prompt_by_id(prompt_id)
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt não encontrado")
    return prompt

@router.put("/prompts/{prompt_id}", response_model=PromptResponse)
async def update_prompt(prompt_id: str, update_data: PromptUpdateRequest):
    updated_prompt = prompt_service.update_prompt(prompt_id, update_data)
    if not updated_prompt:
        raise HTTPException(status_code=404, detail="Prompt não encontrado")
    return updated_prompt

@router.delete("/prompts/{prompt_id}")
async def delete_prompt(prompt_id: str):
    if not prompt_service.delete_prompt(prompt_id):
        raise HTTPException(status_code=404, detail="Prompt não encontrado")
    return {"message": "Prompt apagado com sucesso"}

@router.delete("/prompts")
async def delete_all_prompts():
    count = prompt_service.delete_all_prompts()
    return {"message": f"{count} prompts apagados com sucesso"} 