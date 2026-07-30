from pathlib import Path

file = Path("resume.pdf")

print("File Name :", file.name)
print("File Stem :", file.stem)
print("Extension :", file.suffix)