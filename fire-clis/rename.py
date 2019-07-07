import os
import shutil
import fire


def rename(path=os.getcwd()):
    "Rename files in the same directory."

    filenames = os.listdir(path)
    ignore = ['.git', '.gitignore', 'README.md', 'rename.py']

    for filename in filenames:
        if filename not in ignore:
            shutil.move(filename, filename.replace(" ", "-").lower())


if __name__ == '__main__':
    fire.Fire(rename)
