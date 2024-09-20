import subprocess
import os
from rich import print
def checkIfPullNeeded():
    print(f"[green]Pulling from {os.getcwd()}")
    # Fetch the latest changes from the remote
    subprocess.run(['git', 'fetch'], check=True)
    
    # Get the local and remote head commit hashes
    local_commit = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip()
    remote_commit = subprocess.check_output(['git', 'rev-parse', '@{u}']).strip()

    if local_commit == remote_commit:
        print("[red]Your branch is up to date with the remote.")
        return False
    else:
        print("[green]Pull needed. Your branch is behind the remote.")
        return True
