import os
from rich import print


def checkForGitDir():
    if os.path.isdir('.git'):
        return True
    else:
        print('[red]This is not a git repository')
        exit()
