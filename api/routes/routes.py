from fastapi import APIRouter, HTTPException
from ..lib import chains
from ..schemas import prompt


router = APIRouter()


@router.post("/prompt")
async def get_prompt_response(request: prompt.PromptRequest):
    try:
        response = chains.openai_request(request.prompt)
        return {"response": response}
    
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)