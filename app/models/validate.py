"""
what does this do: validate file path
input: path obtained from user
flow: userinput -> here
"""

#imports
from pathlib import Path
from config import MAX_CHARS

def read_code(path: Path) -> str:
    code = path.read_text(encoding="utf-8")
    if (len(code)>MAX_CHARS):
        raise ValueError("What evne")
    if not code.strip():
        raise ValueError("[File is empty]")
    return code
