import os
from pathlib import Path

print("Enter path")
path = input()
print('\n')


def check_existance(path_to_check):
    if os.path.exists(path_to_check):
        print("file exist")
    else:
        print("file dont exist")


def file_creation(path_to_create):
    if not os.path.exists(path_to_create):
        os.makedirs(path_to_create)
        print("file created")
    else:
        print("file already exist")


source_file = Path(path)
with open(source_file, "r", encoding="utf-8") as file:
    for line in file:
        if line.endswith('\n'):
            line = line.rsplit("\n")
            new_path = line[0]
            print(new_path)
            # new_path.encode('utf-8')
            check_existance(new_path)
            file_creation(new_path)
        else:
            new_path = line
            print(new_path)
            check_existance(new_path)
            file_creation(new_path)
