"""
what does this do: model for validating agent response
"""
from pydantic import BaseModel

class Response(BaseModel):
    bugs: list[str]
    maintainability: list[str]
    performance: list[str]
    suggestions: list[str]
    summary: str