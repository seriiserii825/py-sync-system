import os
from rich import print
from modules.checkForGitDir import checkForGitDir
from modules.checkIfPullNeeded import checkIfPullNeeded
from rich.panel import Panel

def pipInstall():
    if not os.path.exists('venv'):
        os.system('python3 -m venv venv')
        os.system('source venv/bin/activate')
        os.system('python3 -m pip install --upgrade pip')
        os.system('python3 -m pip install -r requirements.txt')
    else:
        os.system('source venv/bin/activate')
        os.system('python3 -m pip install -r requirements.txt')

def gitModules():
    os.system('git submodule init')
    os.system('git submodule update')
    # get submodule dirs from .gitmodules
    with open('.gitmodules') as f:
        lines = f.readlines()
        for line in lines:
            if 'path' in line:
                print(f'line: {line}')
                path = line.split('=')[1].strip()
                print(f'path: {path}')
                if path == 'libs':
                    os.chdir(path)
                    gitPull()
                    os.chdir('..')
                else:
                    print(f'[red]Error: libs not found')
                    os.chdir('..')

def gitPull():
    print(Panel(f"Pulling from {os.getcwd()}", title="Git Pull", style="blue"))
    if checkForGitDir():
        # check for gitmodules
        if os.path.exists('.gitmodules'):
            gitModules()
        result = checkIfPullNeeded()
        if result:
            os.system('git pull')
            # check for python files
            if os.path.exists('requirements.txt'):
                pipInstall()


