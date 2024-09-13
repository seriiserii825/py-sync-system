import os
from git import Repo
file_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'repos.txt')
os.system(f"rm {file_path}")
def reposToFile(file_path):
    print('Finding git repos')
    command = f"find ~ -maxdepth 5 -name \".git\" -type d  > {file_path}"
    os.system(command)
    # os.system(f"sed -i '/cache/d' {file_path}")
    # os.system(f"sed -i '/yay/d' {file_path}")
    # os.system(f"sed -i 's/.git//g' {file_path}")
    os.system(f"bat {file_path}")
def gitCommit():
    print('Committing')
    print('1) Lazygit')
    print('2) Commit')
    choice = input('Enter your choice: ')
    repo = Repo('.')
    if choice == '1':
        os.system('lazygit')
        gitCommit()
    elif choice == '2':
        print('Commit')
        commit_message = input('Enter commit message: ')
        repo.git.add(update=True)
        repo.git.commit('-m', commit_message)
        repo.git.push()
        return
    else:
        print('Invalid Choice')
        gitCommit()
def gitPush(file_path):
    print('Pushing')
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            os.chdir(line)
            repo = Repo('.')
            if repo.is_dirty() or len(repo.untracked_files) > 0:
                print(os.getcwd())
                gitCommit()
def gitPull(file_path):
    print('Pulling')
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            os.chdir(line)
            repo = Repo('.')
            print(os.getcwd())
            command = f"git remote update && git status -uno | grep -q 'Your branch is behind'"
            result = os.system(command)
            if result == 0:
                print('Pulling')
                repo.git.pull()
    # rm = f"rm {file_path}"
    # os.system(rm)


def menu():
    reposToFile(file_path)
    # gitPush(file_path)
    # gitPull(file_path)
menu()
