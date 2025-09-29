# import csv
import file_ops
from pathlib import Path

# Define the workspace and CSV file path
workspace = Path("workspace")
csv_file = workspace / "contacts.csv"

# Function to get participant's name with validation
def get_name():
    while True:
        try:
            name = input("Enter your name: ").strip()
            if name == "":  # Name cannot be empty
                print("Sorry, name cannot be empty")
            elif name.isdigit():  # Name cannot be all numbers
                print("Name cannot be a number")         
            else:
                return name  # Valid name
        except ValueError:
            print("\nName cannot be a number")
        except Exception:
            print("\nAn Unexpected Error Occured")

# Function to get participant's age with validation
def get_age():
    while True:
        try:
            age = input("Enter your age: ").strip()
            if not age.isnumeric():  # Age must be numeric
                print("Please enter only numbers for age")
            else:
                age_input = int(age)
                if age_input <= 0:  # Age must be positive
                    print("Age cannot be zero or a negative number") 
                else:
                    return age_input  # Valid age
        except Exception:
            print("\nAn unexpected error occurred")

# Function to get participant's phone number with validation
def get_phone():
    while True:
        try:
            phone = input("Enter your phone number: ").strip()
            if not phone.isnumeric():  # Phone number must be digits only
                print("Phone number must not have any letters")
            elif len(phone) != 11:  # Must be exactly 11 digits
                print("Sorry, your phone number must be 11 digits")
            else:
                return phone  # Valid phone number
        except Exception:
            print("\nAn unexpected error occurred")

# Function to get participant's track with validation
def get_track():
    while True:
        try:
            track = input("Enter your track: ").strip()
            if track == "":  # Track cannot be empty
                print("Sorry, track cannot be empty")
            elif track.isdigit():  # Track must have letters, not digits only
                print("Track must contain only letters")
            else:
                return track  # Valid track
        except Exception:
            print("\nAn Unexpected error occurred")

# Main function controlling the flow of the program
def main():
    print("Welcome to Raiza Contact saver")
    while True:
        try:
            # Get participant details
            name = get_name()
            age = get_age()
            phone = get_phone()
            track = get_track()

            # Store participant details in a dictionary
            participant = {
                "Name": name,
                "Age": age,
                "Phone": phone,
                "Track": track
            }
            try:
                # Save participant details to CSV file
                file_ops.save_participant(csv_file, participant)
                print("Participant data written to CSV file!")

                # Ask if user wants to add another participant
                add_new = input("Do you want to add another participant? (Enter yes or no): ").lower()
                if add_new != "yes":  # If not yes, display saved contacts and exit
                    print("Here is the list of contact saved: ")
                    file_ops.load_participant(csv_file)
                    break
            except Exception:
                print("\nAn unexpected error occurred while saving the data") 
        except Exception:
            print("\nAn unexpected error occurred")                

# Run the program
if __name__ == "__main__":
    main()
