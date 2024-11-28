

user_name = input("Enter Name to Find information: ")

with open("personal_information.txt", "r") as f:
    user_information = f.read()
    print(user_information)



