from pathlib import Path

dirpath = r'/home/g/lab/lab1/files'
if dirpath:
    root = Path(dirpath)
else:
    root = Path('.')

with open('Not_exist.txt', 'r') as file:
    for string in file:
        (root/string[:-1]).touch()
