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

contacts = []

print("\nAll saved contacts:")
with open("contacts.csv", "r") as file:
    for line in file:
        name, telephone, email = line.rstrip().split(",")
        
        contact = {
            "name": name,
            "telephone": telephone,
            "email": email
        }

        contacts.append(contact)

sorted_contacts = sorted(contacts, key=lambda contact: contact["name"].lower())


print("\nAll Contacts (sorted by name):")
for contact in sorted_contacts:
    print(f"Name: {contact['name']}, Phone: {contact['telephone']}, Email: {contact['email']}")

