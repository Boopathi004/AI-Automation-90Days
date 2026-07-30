import os

for root, folders, files in os.walk("."):
    print("Folder:", root)

    for folder in folders:
        print(" Subfolder:", folder)

    for file in files:
        print(" File:", file)