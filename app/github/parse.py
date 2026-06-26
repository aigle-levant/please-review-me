
# imports
from wrapper import fetch_open_prs
from github.PullRequest import PullRequest
from models.models import ChangedFile

def choose_pr(prs: list[PullRequest]) -> PullRequest:
    li = []
    for pr in prs:
        print(f"#{pr.number} - {pr.title} ({pr.user.login})")
    while True:
        num = int(input("PR number: "))
        if not num.isdigit():
            print("Please enter a valid number.")
            continue
        for pr in prs:
            if pr.number == num:
                return pr
        print("PR not found.")
        continue