import os
from pathlib import Path

print("Enter path to file that contains required paths")
# paths in file must be written in the correct way
path = input()
print('\n')


def check_existance(path_to_check):
    if os.path.exists(path_to_check):
        print("file exist")
    else:
        print("file dont exist")


def path_creation(path_to_create):
    if not os.path.exists(path_to_create):
        os.makedirs(path_to_create)
        print("file created")
    else:
        print("file already exist")


def file_creation(f_path: str, iterator: str):
    file_path = os.path.join(f_path, f"{iterator}.txt")
    new_file = open(file_path, "a", encoding="utf-8")
    new_file.close()


def service_op(a: str, itr: int):
    check_existance(a)
    path_creation(a)
    file_creation(a, str(itr))


def file_reader_n_creator(checked_path):
    source_file = Path(checked_path)
    i = 1
    with open(source_file, "r", encoding="utf-8") as file:
        for line in file:
            if line.endswith('\n'):
                line = line.rsplit("\n")
                new_path = line[0]
                print(new_path)
                # new_path.encode('utf-8')
                service_op(new_path, i)
                i += 1
            else:
                new_path = line
                print(new_path)
                service_op(new_path, i)
                i += 1


if os.path.exists(path):
    file_reader_n_creator(path)
else:
    print("Path doesn`t exist or entered wrong path")
