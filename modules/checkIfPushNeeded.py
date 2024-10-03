import os
import git

def checkIfPushNeeded():
    # if exists .gpgrc and it's not empty
    my_repo = git.Repo('.')
    if os.path.exists('.gpgrc') and os.path.getsize('.gpgrc') > 0:
        return True
    elif my_repo.is_dirty(untracked_files=True):
        return True
    else:
        return False
