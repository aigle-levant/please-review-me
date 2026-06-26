"""
what does this do: github wrapper setup
input:
output:
flow: 
"""

# imports
from ..config import gh

def fetch_open_prs(repo_name: str):
    try:
        repo = gh.get_repo(repo_name)
        prs = list(repo.get_pulls(state="open"))

        if not prs:
            return None
        return prs
    except Exception as e:
        raise RuntimeError(f"Failed to fetch PRs: {e}")