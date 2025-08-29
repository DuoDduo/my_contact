import csv
from pathlib import Path

# Define the folder to store the CSV file
workspace = Path("workspace")
csv_file = workspace / "contacts.csv"  # Path to the CSV file
workspace.mkdir(exist_ok=True)  # Create folder if it doesn't exist

# Define the column names for the CSV file
column = ["Name", "Age", "Phone", "Track"]

def save_participant(csv_file, participant):
    if type(participant)==dict:
     participant=[participant]
    with open(csv_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=column)
        # writer.writeheader()
        writer.writerow(participant)
print("Details succesfully saved")        

def load_participant(csv_file):
 with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row_number, row in enumerate(reader):
                if row_number == 0:  # First row is the header
                    print(f"Headers: {' | '.join(row)}")  # Print headers nicely
                    print("-" * 40)  # Print a line separator
                else: 
                    name, age, phone, track = row
                    print(f"{name} {age} {phone} {track}")  # Print row data in a readable f
print("No participants found yet.")