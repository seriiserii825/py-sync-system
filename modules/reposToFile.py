import os

def reposToFile(file_path):
    os.system(f"rm {file_path}")
    print('[green]Finding git repos')
    command = f"find ~ -maxdepth 8 -name \".git\" -type d  > {file_path}"
    os.system(command)
    os.system(f"sed -i '/cache/d' {file_path}")
    os.system(f"sed -i '/yay/d' {file_path}")
    os.system(f"sed -i '/autoload/d' {file_path}")
    os.system(f"sed -i '/oh-my-zsh/d' {file_path}")
    os.system(f"sed -i '/powerlevel10k/d' {file_path}")
    os.system(f"sed -i '/Trash/d' {file_path}")
    os.system(f"sed -i '/advanced-custom-fields-wpcli/d' {file_path}")
    os.system(f"sed -i 's/.git//g' {file_path}")
    # os.system(f"bat {file_path}")

