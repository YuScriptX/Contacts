while True:

    name = str(input("Enter your name: "))

    if name == "stop":
        break

    telephone = input("Enter your telephone number: ")
    email = input("Enter your email: ")

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



print("\nAll saved contacts:")
with open("contacts.csv", "r") as file:
    for line in file:
        name, telephone, email = line.rstrip().split(",")
        print(f"Name: {name}, Phone: {telephone}, Email: {email}")
