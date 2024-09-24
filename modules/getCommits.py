import os
import subprocess
from datetime import datetime
from rich import print
from rich.panel import Panel

from modules.getLocalProjects import getLocalProjects
from modules.gitCommitToBuffer import gitCommitToBuffer
def getCommits(file_path, projects=False):
    today_projects = []
    lines = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            lines.append(line)
    if projects:
        lines = getLocalProjects(lines)
    for line in lines:
        os.chdir(line)
        today_date = datetime.today().strftime('%Y-%m-%d')
        # show user, time when commit was done, and commit message
        command = [
                "git", "log",
                f'--since={today_date} 00:00:00', f'--until={today_date} 23:59:59',
                '--pretty=format:%an: %cd: %s'
                ]
        result = subprocess.run(command, capture_output=True, text=True)

        if result.stdout:
            today_projects.append(line)
            #color result.stdout
            print(Panel(f"[green]{result.stdout}", title=line))
    copy_to_buffer = input("Would you like to copy the commits to the clipboard? [y/n] ")
    if copy_to_buffer.lower() == 'y':
        for line in today_projects:
            print(Panel(f"[blue]Changing directory to {line}"))
            os.chdir(line)
            gitCommitToBuffer()
            input("Press Enter to continue...")

