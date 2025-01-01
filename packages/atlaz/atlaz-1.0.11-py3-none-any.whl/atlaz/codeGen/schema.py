from typing import Optional
from pydantic import BaseModel

class CodeGenRequest(BaseModel):
    instruction: str
    code: str
    openai_api_key: str
    model_choice: Optional[str] = "o1"