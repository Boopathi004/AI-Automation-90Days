from pathlib import Path

file = Path("sample.txt")

if file.exists():
    print(file.stat().st_size, "bytes")