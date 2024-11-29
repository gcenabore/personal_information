
# !!!code needs more revision, and update.!!!


user_name = input("Enter Name to Find information: ")
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

    # user_information = f.read()
    # print(user_information)




