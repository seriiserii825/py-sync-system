import subprocess
def checkIfPushNeeded():
    subprocess.run(['git', 'fetch'], check=True)
    
    remote_commit = subprocess.check_output(['git', 'rev-parse', '@{u}'], text=True).strip()
    base_commit = subprocess.check_output(['git', 'merge-base', '@', '@{u}'], text=True).strip()

    if remote_commit == base_commit:
        print("You have unpushed local changes.")
        return True
    else:
        print("Your branch has diverged from the remote.")
        return True
