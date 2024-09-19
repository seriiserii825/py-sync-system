import os

from modules.checkForGitDir import checkForGitDir
from modules.checkIfPullNeeded import checkIfPullNeeded

def pipInstall():
    if not os.path.exists('venv'):
        os.system('python3 -m venv venv')
        os.system('source venv/bin/activate')
        os.system('python3 -m pip install --upgrade pip')
        os.system('python3 -m pip install -r requirements.txt')
        os.system('deactivate')
    else:
        os.system('source venv/bin/activate')
        os.system('python3 -m pip install -r requirements.txt')
        os.system('deactivate')

def gitModules():
    os.system('git submodule init')
    os.system('git submodule update')
    # get submodule dirs from .gitmodules
    with open('.gitmodules') as f:
        lines = f.readlines()
        for line in lines:
            if 'path' in line:
                path = line.split('=')[1].strip()
                os.chdir(path)
                gitPull()
                os.chdir('..')

def gitPull():
    if checkForGitDir():
        result = checkIfPullNeeded()
        if result:
            os.system('git pull')
            # check for python files
            if os.path.exists('requirements.txt'):
                pipInstall()
            # check for gitmodules
            if os.path.exists('.gitmodules'):
                gitModules()


