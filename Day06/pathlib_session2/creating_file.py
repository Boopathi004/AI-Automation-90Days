from pathlib import Path

file = Path("sample.txt")

file.touch(exist_ok=True)

print("File Created")