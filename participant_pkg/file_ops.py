import csv
from pathlib import Path
# Write data to CSV file
workspace = Path("workspace")
csv_file= workspace / "contacts.csv"

def save_participant(csv_file,participant):
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(participant)  # Write all rows at once

print("Particicpant data written to CSV file!")



def load_participant(csv_file):
    print("\nReading CSV file:")
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        
        for row_number, row in enumerate(reader):
            if row_number == 0:  # Header row
                print(f"Headers: {' | '.join(row)}")
                print("-" * 40)
            else:  # Data rows
                name, age, phone, track = row
                print(f"{name} {age} {phone} {track}")