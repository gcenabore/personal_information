
# !!!code needs more revision, and update.!!!


user_name = input("Enter Name to Find information: ")
found = False

with open("personal_information.txt", "r") as f:
    for line in f:
        if user_name in line:
            found = True
            print("information found")
            print(line.strip())

            for _ in range(4):
                print(next(f).strip())
            break

if not found:
    print("no information found.")

    # user_information = f.read()
    # print(user_information)




