import os

from git import Repo
from rich import print

from modules.gitCommit import gitCommit
def gitPush(file_path):
    print('[blue]Pushing')
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            print(f'Pushing {line}')
            os.chdir(line)
            repo = Repo('.')
            if repo.is_dirty() or len(repo.untracked_files) > 0:
                print(os.getcwd())
                gitCommit()
