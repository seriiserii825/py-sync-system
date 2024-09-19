import os


def checkForGitDir():
    return os.path.isdir('.git')
