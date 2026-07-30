from pathlib import Path

file = Path("notes.md")

if file.exists():
    print("File Exists")
else:
    print("File Not Found")