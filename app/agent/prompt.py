"""
what does this do: builds prompt for ai agent
input: validated code
flow: userinput -> validate -> here
"""

def agent_prompt(
    filename: str,
    status: str,
    patch: str,
    persona: str,
) -> str:
    return f"""
{persona}

You are reviewing a GitHub Pull Request.

Your task is to review ONLY the changes shown below.

Rules:
1. Review ONLY the provided patch.
2. Do not speculate about code outside the patch.
3. If there isn't enough context, explicitly say so.
4. Prioritize correctness over style.
5. If you find no issues, say so.
6. Return ONLY valid JSON.
7. Do not use Markdown.
8. Do not wrap the JSON inside ``` blocks.

Return this JSON schema exactly:


File:
{filename}

Status:
{status}

Git Diff:
{patch}

{{
    "bugs": [],
    "maintainability": [],
    "performance": [],
    "suggestions": [],
    "summary": ""
}}
"""