import git
from rich import print
def checkIfPullNeeded(repo_path='.'):
    # Open the repository
    repo = git.Repo(repo_path)
    # Fetch latest changes from the remote
    repo.remotes.origin.fetch()
    # Get the local and remote commit objects
    local_commit = repo.head.commit
    remote_commit = repo.remotes.origin.refs[repo.active_branch.name].commit
    # Compare local and remote commits
    if local_commit == remote_commit:
        print("[red]Your branch is up to date with the remote.")
        return False
    else:
        print("[green]Pull needed. Your branch is behind the remote.")
        return True
