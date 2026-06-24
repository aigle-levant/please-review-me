"""
what does this do: this is the driver code.
"""
# imports
from ollama import generate
from prompt import build_prompt
from models import Response

prompt = build_prompt()

def review() -> Response:
    response = generate(
    model="qwen3:8b",
    prompt=prompt
    )
    return Response.model_validate_json(response.response)