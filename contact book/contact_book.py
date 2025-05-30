# empty dictionary
contacts = {}

# user can exit then stop the program
while True:
    print("\n Contact Book App")
    print('1. Create Contact')
    print('2. View Contact')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contact')
    print('7. Exit')

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print("Contact created successfully!")

    elif choice == '2':
        if not contacts:
            print("No contacts found.")
            continue
        print("\nContacts:")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("-" * 20)

    elif choice == '3':
        name = input("Enter name: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    elif choice == '4':
        name = input("Enter name: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == '5':
        name = input("Enter name: ")
        if name in contacts:
            details = contacts[name]
            print(f"Name: {name}")
        
        else:
            print("Contact not found.")

    elif choice == '6':
        count = len(contacts)
        print(f"Total contacts: {count}")

    elif choice == '7':
        print("Exiting Contact Book App. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
        