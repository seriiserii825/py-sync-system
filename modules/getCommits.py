import os
import subprocess
from datetime import datetime
from rich import print
from rich.panel import Panel
def getCommits(file_path):
    print('[blue]Pushing')
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            os.chdir(line)
            today_date = datetime.today().strftime('%Y-%m-%d')

            # show just commit message
            command = [
                    "git", "log",
                    f'--since={today_date} 00:00:00', f'--until={today_date} 23:59:59',
                    '--pretty=format:%s'
                    ]
            # command = [
            #         "git", "log",
            #         f'--since={today_date} 00:00:00', f'--until={today_date} 23:59:59',
            #         '--pretty=format:%h - %an: %s'
            #         ]

            result = subprocess.run(command, capture_output=True, text=True)

            if result.stdout:
                #color result.stdout
                print(Panel(f"[green]{result.stdout}", title=line))

