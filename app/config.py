"""
what does this do: config settings for all files in this repo
"""

# imports
from rich.console import Console
from github import Github
from github import Auth
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

auth = Auth.Token(TOKEN)

gh = Github(auth=auth)

console = Console()
li = ["stop", "quit", "exit"]
MAX_CHARS = 100000
MODEL = "qwen3:8b"
