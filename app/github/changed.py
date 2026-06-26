
from github.PullRequest import PullRequest
from models.models import ChangedFile

def fetch_changed_file(pr: list[PullRequest])->list[ChangedFile]:
    li = []
    for file in pr.get_files():
        li.append(
        ChangedFile(
            filename=file.filename,
            status=file.status,
            additions=file.additions,
            deletions=file.deletions,
            patch=file.patch,
        )
    )
    return li