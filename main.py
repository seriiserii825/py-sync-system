import os
from rich.console import Console

from modules.gitPull import gitPull
from modules.gitPush import gitPush
from modules.reposToFile import reposToFile

file_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'repos.txt')
console = Console()

def menu():
    reposToFile(file_path)
    action = console.input("[green]Push[/] or [blue]Pull[/]? (push/pull): ")
    if action == "push":
        gitPush(file_path)
    elif action == "pull":
        gitPull(file_path)
    else:
        console.print("[red]Invalid option. Please try again.")
        menu()
menu()
