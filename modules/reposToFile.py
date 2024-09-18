import os

def reposToFile(file_path):
    print('[green]Finding git repos')
    command = f"find ~ -maxdepth 8 -name \".git\" -type d  > {file_path}"
    os.system(command)
    os.system(f"sed -i '/cache/d' {file_path}")
    os.system(f"sed -i '/yay/d' {file_path}")
    os.system(f"sed -i '/autoload/d' {file_path}")
    os.system(f"sed -i 's/.git//g' {file_path}")
    # os.system(f"bat {file_path}")

