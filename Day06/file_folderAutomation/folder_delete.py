import os

folder_name="mini_project"

if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print("folder is deleted ")
else:
    print("folder is not found pls check the foldername ")