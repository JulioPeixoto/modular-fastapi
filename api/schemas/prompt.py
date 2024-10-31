from pydantic import BaseModel, validator

class PromptRequest(BaseModel):
    prompt: str

    @validator('prompt')
    def prompt_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError('O prompt não pode ser vazio.')
        return value
