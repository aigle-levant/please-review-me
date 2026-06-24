"""
what does this do: this has prompts!
"""
# imports
from pathlib import Path

two = """
def twosum(arr,k):
    n = arr.size()
    i = 0
    j = 1
    while (i<n):
        if i!=k:
            return True
"""

def build_prompt() -> str:
    return f"""
You are a senior software engineer.

Review code for:
- Bugs
- Maintainability
- Performance

Return ONLY valid JSON with a cheerful tone, a sarcastic tone or a tone of a concerned parent, depending on how horrible the code looks.

{{
  "bugs": [],
  "maintainability": [],
  "performance": [],
  "suggestions": [],
  "summary": ""
}}

Code:
{two}
"""