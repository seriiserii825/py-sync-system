import os
from rich.console import Console

from libs.richTable import richTable
from modules.getCommits import getCommits
from modules.gitPullAll import gitPullAll
from modules.gitPushAll import gitPushAll
from modules.reposToFile import reposToFile

file_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'repos.txt')
console = Console()

def syncGit():
    reposToFile(file_path)
    table_title = "Git Repository Manager"
    table_columns = ["Option", "Description"]
    table_rows = [
        ["[green]commits[/]", "Push changes to the remote repository."],
        ["[blue]push[/]", "Push changes to the remote repository."],
        ["[red]pull[/]", "Pull changes from the remote repository."]
    ]
    richTable(table_title, table_columns, table_rows)
    action = console.input("[cyan]What would you like to do? ")
    if action == "push":
        gitPushAll(file_path)
    elif action == "pull":
        gitPullAll(file_path)
    elif action == "commits":
        getCommits(file_path)
    else:
        console.print("[red]Invalid option. Please try again.")
        exit()
