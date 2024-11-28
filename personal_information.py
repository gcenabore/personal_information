from datetime import datetime

def collect_information():

    def validate_email(email):
        return "@" in email and "." in email
    
    valid_skin_tone = ["Fair skin", "Medium skin", "Light brown skin", "Brown skin", "Black skin"]

    blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    with open("personal_information.txt", "a") as file:        

        while True:

            first_name = input("Please enter your First Name: ")
            surname = input("Please enter your Surname: ")

            full_name = first_name + surname

            while True:
                age = input("Please enter your Age: ")

                if age.isdigit():
                    digit = int(age)
                    break
                else:
                    print("Invalid: enter a digit age")
                        
            while True: 
                date_of_birth = input("Please enter your Birth date: ")
                try:
                    datetime.strptime(date_of_birth, "%m/%d/%Y")
                    break
                except ValueError:
                    print("Invalid: Pleaes enter your Birth date in this format (MM/DD/YYYY).")
                            
            while True:
                phone_number = input("Please enter your Phone number: ")

                if phone_number.isdigit() and len(phone_number) == 11:
                    number = int(phone_number)
                    break
                else:
                    print("Invalid: type a valid phone number (11 digits).")

            email = input("Please enter your email: ")
            while not validate_email(email):
                print("Invalid format. Please try again.")
                email = input("Enter email: ")
                
            nationality = input("Enter your nationality: ")

            while True:
                complexion = input("Enter your complexion (Fair skin/Medium skin/Light brown skin/Brown skin/Black skin): ")
                if complexion in valid_skin_tone:
                    break
                else:
                    print("Invalid. Try again.")
            while True:
                blood_type = input("Enter your blood type: ")
                if blood_type in blood_types:
                    break
                else:
                    print("Invalid. Try again. choose a valid blood type (A+/A-/B+/B-/AB+/AB-/O+/O-)")
                        
            weight = input("Enter your weight in Kg: ")

            height = input("Enter your height in cm: ")
        
            another_entry = input("Do you want to enter another person? (Yes/No): ").strip().lower()
            if another_entry != "yes":
                break

            file.write(f"Full name: {full_name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Birthday: {date_of_birth}\n")
            file.write(f"Phone number: {phone_number}\n")
            file.write(f"email: {email}\n")
            file.write(f"Nationality: {nationality}\n")
            file.write(f"Complexion: {complexion}\n")
            file.write(f"Blood type: {blood_type}\n")
            file.write(f"Weight: {weight}\n")
            file.write(f"Height: {height}\n")
            file.write("-" * 100 + "\n")
            
collect_information() 