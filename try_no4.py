import os

# print("import path:")
# unchecked_path = input()


# if os.path.exists(unchecked_path):
#     print("correct path")
#     default_path = unchecked_path
# else:
#     print("wrong path")


with open(r"d:\Python project\files_creator\New Sample.txt", "r") as file:
    # добавить в переменную текст проверку на пропуски лишние(новые строки)
    for line in file:
        if line.endswith('\n'):
            line = line.rsplit("\n")
            new_path = line[0]
            print(new_path)
        else:
            new_path = line
            print(new_path)

        os.makedirs(new_path)

        # print(line)
        # print(r"d:\Test Folder\папка\new_file — копия (2).txt")
