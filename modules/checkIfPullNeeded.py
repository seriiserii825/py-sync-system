import subprocess
def checkIfPullNeeded():
    subprocess.run(['git', 'fetch'], check=True)
    
    # Check the status between local and remote
    local_commit = subprocess.check_output(['git', 'rev-parse', '@'], text=True).strip()
    remote_commit = subprocess.check_output(['git', 'rev-parse', '@{u}'], text=True).strip()
    base_commit = subprocess.check_output(['git', 'merge-base', '@', '@{u}'], text=True).strip()

    if local_commit == remote_commit:
        print("Your branch is up to date with the remote.")
        return False
    elif local_commit == base_commit:
        print("You need to pull the latest changes.")
        return True
    elif remote_commit == base_commit:
        print("You have unpushed local changes.")
        return False
    else:
        print("Your branch has diverged from the remote.")
        return True

