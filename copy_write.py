import os
import shutil

source = input("Enter the source directory: ")
target = input("Enter the target directory: ")

print(source)
print(target)

path = []

for root, dirs, files in os.walk(source):
    for file in files:
        path_file = os.path.join(root, file)
        shutil.copy2(path_file, target)
        path.append(path_file)
    print(path)

