"""
what does this do: prepares agent for responding
input: prompt
flow: userinput -> validate -> prompt -> here
"""

# imports
from ollama import generate
from models.models import Response
from config import MODEL

def agent_response(q: str) -> Response:
    res = generate(model=MODEL, prompt=q)
    return Response.model_validate_json(res.response)