from pathlib import Path

BASE_DIR = Path(__file__).parent
print(BASE_DIR)

# division example
print(BASE_DIR / 'data' / 'file.txt')