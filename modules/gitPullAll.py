import os

from modules.checkIfPullNeeded import checkIfPullNeeded
def gitPullAll(file_path):
    print('[green]Pulling')
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            os.chdir(line)
            result = checkIfPullNeeded()
            if result:
                os.system('git pull')
