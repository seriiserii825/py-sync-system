import subprocess
import os
import sys

def pip_install():
    if not os.path.isdir("venv"):
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        activate_venv = "source venv/bin/activate"
        subprocess.run(activate_venv, shell=True, check=True)
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)

def gitClone():
    clipboard = subprocess.check_output("xclip -o -selection clipboard", shell=True, text=True).strip()

    if "github.com" in clipboard or "bitbucket.org" in clipboard:
        print(clipboard)

        git_command = f"git clone {clipboard} --single-branch"
        if "bitbucket.org" in clipboard:
            git_command = f"{clipboard}"
        subprocess.run(git_command, shell=True, check=True)

        # Change directory to the cloned repo
        repo_name = os.path.basename(clipboard).replace(".git", "")
        os.chdir(repo_name)

        # Check for and update submodules if present
        if os.path.isfile(".gitmodules"):
            subprocess.run("git submodule update --init --recursive", shell=True, check=True)
            subprocess.run(
                "git submodule foreach 'branch=$(git branch -r | grep -m1 origin/HEAD | sed \"s/.*origin\\///\") && git checkout $branch && git pull origin $branch'",
                shell=True, check=True
            )

        # Check for requirements.txt and run pip install if it exists
        if os.path.isfile("requirements.txt"):
            pip_install()

    else:
        print("Clipboard does not contain a Git repository URL.")

