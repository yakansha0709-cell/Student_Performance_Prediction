import csv
import random
from pathlib import Path

random.seed(42)

project_dir = Path(__file__).resolve().parent
dataset_path = project_dir / "static" / "dataset" / "student.csv"
dataset_path.parent.mkdir(parents=True, exist_ok=True)

with dataset_path.open("w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Study_Hours",
        "Attendance",
        "Previous_Marks",
        "Final_Marks"
    ])

    for i in range(100):

        study_hours = random.randint(1, 10)
        attendance = random.randint(50, 100)
        previous_marks = random.randint(30, 95)

        final_marks = (
            study_hours * 3
            + attendance * 0.25
            + previous_marks * 0.35
            + random.randint(-8, 8)
        )

        final_marks = max(0, min(100, round(final_marks)))

        writer.writerow([
            study_hours,
            attendance,
            previous_marks,
            final_marks
        ])

print("100 Students Dataset Created Successfully!")