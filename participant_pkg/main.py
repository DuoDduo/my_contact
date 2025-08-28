import csv
import file_ops
from pathlib import Path

workspace = Path("workspace")
csv_file= workspace / "contacts.csv"

def get_name():
    while True:
        try:
           name = input("Enter your name: ").strip()
           if name != "" :
            return name 
           elif name.isdigit():
               print("Name cannot be a number")         
           else:
              print("Sorry, name cannot be empty")
        except ValueError:
            print("\nName cannot be a number")
        except Exception:
         print("\nAn Unexpected Error Occured")

def get_age():
    while True:
        try:
           age = input("Enter your age: ").strip()
           if age.isnumeric():
               age_input=int(age)
               if age_input > 0:
                  return age_input
               else:
                  print("Sorry, age cannot be zero ")
           else:
              print("Please enter only number for age ")   
        except Exception:
            print("\nAn unexpected error occurred")

def get_phone():
    while True:
        try:
            phone = input("Enter your phone number: ").strip()
            if phone.isnumeric():
                  if len(phone)== 11:
                     return phone
                  else:
                     print("Sorry, your phone number must be 11 ")
            else:
               print("Sorry, your phone number must be 11 ")
        except Exception:
            print("\nAn unexpected error occurred")

def get_track():
    while True:
        try:
           track = input("Enter your track: ").strip()
           if track != "" :
            return track        
           else:
              print("Sorry, name cannot be empty")
        except ValueError:
            print("\nName cannot be a number")


def main():
   print("Welcome to Raiza Contact saver")
   while True:
      try:
         name=get_name()
         age=get_age()
         phone= get_phone()
         track= get_track()

         participant={
            "Name":name,
            "Age": age,
            "Phone": phone,
            "Track":track

         }
         try:
            file_ops.save_participant(csv_file, participant)
            
            print("Particicpant data written to CSV file!")
         except Exception:
            print("\nAn unexpected error occurred") 

            add_new=input("Do you want to add another participant? (Enter yes or no)").lower()
            if add_new!="yes":
               break;  
      except Exception:
        print("\nAn unexpected error occurred")                



if __name__ == "__main__":
    main()                     