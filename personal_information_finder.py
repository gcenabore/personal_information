

while True:

    print("!!!TYPE THE USER'S FIRST NAME AND SURNAME TO ACQUIRE THEIR INFORMATION!!!")

    first_name = input("Enter First name: ")
    surname = input("Enter Surname: ")

    user_name = first_name + " " + surname
    found = False

    with open("personal_information.txt", "r") as f:
        for line in f:
            if user_name in line:
                found = True
                print(f"INFORMATION FOUND: Information on {user_name}:")
                print(line.strip())

                for line in range(10):
                    print(next(f).strip())
                print("_" * 100)
                break

    if not found:
        print(f"ERROR: THERE IS NO  EXISTING INFORMATION ON: {user_name}")
    
    retry = input("Do you want to search again? (Yes/No)").strip().lower()
    if retry != "yes":
        break

    # user_information = f.read()
    # print(user_information)




