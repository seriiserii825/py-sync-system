import os
from git import Repo
from rich import print


def gitCommit():
    print('[blue]Committing')
    print('[green]1) Lazygit')
    print('[blue]2) Commit')
    choice = input('Enter your choice: ')
    repo = Repo('.')
    if choice == '1':
        os.system('lazygit')
        gitCommit()
    elif choice == '2':
        print('[green]Commit')
        commit_message = input('Enter commit message: ')
        repo.git.add(update=True)
        repo.git.commit('-m', commit_message)
        repo.git.push()
        return
    else:
        print('Invalid Choice')
        gitCommit()

