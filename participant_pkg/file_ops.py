import csv
from pathlib import Path

# Define the folder to store the CSV file
workspace = Path("workspace")
csv_file = workspace / "contacts.csv"  # Path to the CSV file
workspace.mkdir(exist_ok=True)  # Create folder if it doesn't exist

# Define the column names for the CSV file
fieldnames = ["Name", "Age", "Phone", "Track"]


# Function to save participant(s) into the CSV file
def save_participant(csv_file, participant):
    # Convert dictionary of participant to a list
    if type(participant) == dict:
     participant = [participant]
    # If the file already exists, append new data
    if csv_file.exists():
        with open(csv_file, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerows(participant)
    else:
        # If file doesn't exist, create it and write header first
        print(f"File {csv_file} doesn't exist, Creating it now!")
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(participant)

print("Particicpant data written to CSV file!")


# Function to read and display participants from the CSV file
def load_participant(csv_file):
    print("\nReading CSV file:")
    if csv_file.exists():
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)  # Read the CSV file row by row
            for row_number, row in enumerate(reader):
                if row_number == 0:  # First row is the header
                    print(f"Headers: {' | '.join(row)}")  # Print headers nicely
                    print("-" * 40)  # Print a line separator
                else: 
                    name, age, phone, track = row
                    print(f"{name} {age} {phone} {track}")  # Print row data in a readable format
    else:
        print("No participants found yet.")

   
      

