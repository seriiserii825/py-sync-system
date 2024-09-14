import os

from git import Repo
def gitPull(file_path):
    print('[green]Pulling')
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
