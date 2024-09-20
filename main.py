import os
import sys
from rich.console import Console

from libs.richTable import richTable
from modules.gitClone import gitClone
from modules.gitPull import gitPull
from modules.gitPush import gitPush
from modules.syncGit import syncGit

file_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'repos.txt')
console = Console()

def menu():
    args = sys.argv
    args_str = ''

    if len(args) > 1:
        for i in range(1, len(args)):
            args_str += args[i] + ' '
        commit_message = args_str if args_str != '' else ''
    else:
        commit_message = ''

    table_title = "Choose an option"
    table_columns = ["Option", "Description"]
    table_rows = [
        ["[green]1) Sync[/]", "Sync all repositories."],
        ["[blue]2) Push[/]", "Push"],
        ["[yellow]3) Pull[/]", "Pull"],
        ["[green]4) Clone[/]", "Clone"],
    ]
    richTable(table_title, table_columns, table_rows)
    action = console.input("[cyan]What would you like to do? ")
    if action == "1":
        syncGit()
    elif action == "2":
        gitPush(commit_message)
    elif action == "3":
        gitPull()
    elif action == "4":
        gitClone()
    else:
        console.print("[red]Invalid option. Please try again.")
        exit()
menu()
