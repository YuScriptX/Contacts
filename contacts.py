while True:

    name = str(input("Enter your name: "))
    telephone = input("Enter your telephone number: ")
    email = input("Enter your email: ")

    if name == "stop":
        break

    if not telephone.isdigit():
        print("Telephone number must be positive")
        continue

    telephone_int = int(telephone)

    if telephone_int < 0:
        print("Can't be negative")
        continue

    if "@" not in email:
        print("Invalid email")
        continue

    print(f"\nSaved:")
    print(f"Name: {name}")
    print(f"Telephone: {telephone}")
    print(f"Email: {email}")
    

    with open("contacts.csv", "a") as file:
        file.write(f"{name},{telephone},{email}\n")