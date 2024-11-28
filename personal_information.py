

def collect_information():

    while True:
        first_name = input("Please enter your First Name: ")
        surname = input("Please enter your Surname: ")
        age = input("Please enter your Age: ")
        date_of_birth = input("Please enter your Birth date: ")

        while True:
            phone_number = input("Please enter your Phone number: ")

            if len(phone_number) != 11:
                print("Invalid: type a valid phone number (11 digits).")
                break
    
        email = input("Please enter your email: ")

        nationality = input("Enter your nationality: ")
        complexion = input("Enter your complexion: ")
        blood_type = input("Enter your blood type: ")
        weight = input("Enter your weight in Kg: ")
        height = input("Enter your height in cm: ")

collect_information()