import shutil

source = "sample_copy.txt"
destination = "Backup/sample_copy.txt"

shutil.move(source, destination)

print("File moved successfully.")