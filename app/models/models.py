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

class ChangedFile(BaseModel):
    filename: str
    status: str
    additions: int
    deletions: int
    patch: str | None = None