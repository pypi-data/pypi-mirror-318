from typing import Optional
from pydantic import BaseModel

class CodeGenRequest(BaseModel):
    file_contents: list[dict]
    directory_structure: str
    instruction: str
    openai_api_key: str
    model_choice: Optional[str] = "o1"