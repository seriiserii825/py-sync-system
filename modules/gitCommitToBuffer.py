import subprocess
# from plyer import notification
def gitCommitToBuffer():
    # log=$(git log --since="3am" --pretty=tformat:"%s" --reverse > log.log);
    # sed -i 's/feat://' log.log
    # cat log.log | xclip -selection clipboard
    # rm log.log
    # bash code to python
    command = [
            "git", "log",
            "--since=3am", "--pretty=tformat:%s", "--reverse"
            ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.stdout:
        result.stdout = result.stdout.replace('feat:', '')
        command = [
                "xclip", "-selection", "clipboard"
                ]
        result = subprocess.run(command, input=result.stdout, text=True)
        print("[blue]Commits copied to clipboard.")
        # notification.notify(
        #         title="Commits copied to clipboard.",
        #         message=result.stdout,
        #         timeout=10
        #         )

