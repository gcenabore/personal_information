from datetime import datetime

def collect_information():

    while True:
        
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
                number = int(phone_number)

                if len(phone_number) == 11:
                    break
                else:
                    print("Invalid: type a valid phone number (11 digits).")

            
            # email = input("Please enter your email: ")

            # nationality = input("Enter your nationality: ")
            # complexion = input("Enter your complexion: ")
            # blood_type = input("Enter your blood type: ")
            # weight = input("Enter your weight in Kg: ")
            # height = input("Enter your height in cm: ")

collect_information()