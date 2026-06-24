"""
what does this do: pydantic models, for smoother and sexier output
"""
from pydantic import BaseModel

class Response(BaseModel):
    bugs: list[str]
    maintainability: list[str]
    performance: list[str]
    suggestions: list[str]
    summary: str

