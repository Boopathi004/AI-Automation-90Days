import shutil

destination="sample.txt"
copy="sample_copy.txt"

shutil.copy(destination,copy)
print("copy created")