import os
from rich.console import Console

from libs.richTable import richTable
from modules.gitPull import gitPull
from modules.gitPush import gitPush
from modules.syncGit import syncGit

file_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'repos.txt')
console = Console()

def menu():
    table_title = "Choose an option"
    table_columns = ["Option", "Description"]
    table_rows = [
        ["[green]1) Sync[/]", "Sync all repositories."],
        ["[blue]2) Push[/]", "Push changes to the remote repository."],
        ["[yellow]3) Pull[/]", "Pull changes from the remote repository."]
    ]
    richTable(table_title, table_columns, table_rows)
    action = console.input("[cyan]What would you like to do? ")
    if action == "1":
        syncGit()
    elif action == "pull":
        gitPush()
    elif action == "commits":
        gitPull()
    else:
        console.print("[red]Invalid option. Please try again.")
        exit()
menu()
