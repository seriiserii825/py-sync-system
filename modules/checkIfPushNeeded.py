import git

def checkIfPushNeeded():
    my_repo = git.Repo('.')
    if my_repo.is_dirty(untracked_files=True):
        return True
    else:
        return False
