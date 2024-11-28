
# !!!code needs more revision, and update.!!!


user_name = input("Enter Name to Find information: ")

with open("personal_information.txt", "r") as f:
    for line in f:
        if user_name in line:
            found = True
            print("information found")
            print(line)

            for line in range(10):
                print(next(f))
            break


    # user_information = f.read()
    # print(user_information)




