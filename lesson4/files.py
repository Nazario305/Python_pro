import csv
from pathlib import Path

files_dir = Path(__file__).parent / "files"
students_file = files_dir / "students.csv"

files_dir.mkdir(parents=True, exist_ok=True)

if not students_file.exists():
    with open(students_file, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "marks"])
        writer.writeheader()

try:
    with open(students_file, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
        print(data)
except csv.Error as e:
    print(f"Ошибка чтения CSV-файла: {e}")
