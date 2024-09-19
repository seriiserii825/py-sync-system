import os
import sys
from rich import print
from rich.prompt import Prompt

from modules.checkForGitDir import checkForGitDir
from modules.checkIfPushNeeded import checkIfPushNeeded
from utils.decryptFiles import decryptFiles
from utils.encryptFiles import encryptFiles
from utils.tableMenu import tableMenu

user = os.getlogin()

commands = {
        '1': 'feat',
        '2': 'upd',
        '3': 'bug-fix',
        '4': 'fix',
        '5': 'core',
        }



def gitPush():
    args = sys.argv
    args_str = ''

    if len(args) > 1:
        for i in range(1, len(args)):
            args_str += args[i] + ' '

    os.system('git status')
    choose = tableMenu()
    if choose in ['1', '2', '3', '4', '5']:
        encryptFiles()
        commit_message = args_str if args_str != '' else Prompt.ask("Commit message")
        if commit_message == '':
            print('[red]Commit message is required')
            gitPush()
        git_command= f'git add . && git commit -m "{commands[choose]}: {commit_message}" && git push'
        os.system(git_command)
        print('[green]Done')
        decryptFiles()
    else:
        if choose == '6':
            os.system('lazygit')
            gitPush()
        elif choose == '7':
            print('[red]Bye')
            exit()
        else:
            print('[red]Invalid option')
            gitPush()

    if os.path.exists('.gpgrc'):
        if checkIfPushNeeded():
            gitPush()
        else:
            print('[red]No changes to commit')
    else:
        if checkForGitDir():
            if checkIfPushNeeded():
                gitPush()
            else:
                print('[red]No changes to commit')
