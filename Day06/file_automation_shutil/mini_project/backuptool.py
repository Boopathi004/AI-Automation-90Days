import os
import shutil

print("=" * 35)
print("        BACKUP TOOL")
print("=" * 35)

# User Input
source_folder = input("Enter Source Folder : ")
backup_folder = input("Enter Backup Folder : ")

# Check source folder exists
if os.path.exists(source_folder):

    # Check backup folder already exists
    if os.path.exists(backup_folder):

        choice = input("Backup folder already exists.\nOverwrite? (y/n): ")

        if choice.lower() == "y":
            shutil.rmtree(backup_folder)          # Delete old backup
            shutil.copytree(source_folder, backup_folder)
            print("\n✅ Backup Updated Successfully!")

        else:
            print("\n❌ Backup Cancelled.")

    else:
        shutil.copytree(source_folder, backup_folder)
        print("\n✅ Backup Created Successfully!")

else:
    print("\n❌ Source Folder Not Found.")