import os
from rich.console import Console

from libs.richTable import richTable
from modules.gitPull import gitPull
from modules.gitPush import gitPush
from modules.reposToFile import reposToFile

file_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'repos.txt')
console = Console()

def menu():
    reposToFile(file_path)
    table_title = "Git Repository Manager"
    table_columns = ["Option", "Description"]
    table_rows = [
        ["[blue]push[/]", "Push changes to the remote repository."],
        ["[red]pull[/]", "Pull changes from the remote repository."]
    ]
    richTable(table_title, table_columns, table_rows)
    action = console.input("[cyan]What would you like to do? ")
    if action == "push":
        gitPush(file_path)
        menu()
    elif action == "pull":
        gitPull(file_path)
    else:
        console.print("[red]Invalid option. Please try again.")
        menu()
menu()
