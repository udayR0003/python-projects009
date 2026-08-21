# ==========================================
#        CONTACT BOOK MANAGEMENT SYSTEM
# ==========================================

contacts = {}


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if name in contacts:
        print("Contact already exists!")
        return

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n========== CONTACT LIST ==========")

    for name, details in contacts.items():
        print("Name  :", name)
        print("Phone :", details["phone"])
        print("Email :", details["email"])
        print("-" * 35)


def search_contact():
    name = input("Enter name to search: ").strip()

    if name in contacts:
        print("\nContact Found!")
        print("Name  :", name)
        print("Phone :", contacts[name]["phone"])
        print("Email :", contacts[name]["email"])
    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter name to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    phone = input("Enter new phone number: ").strip()
    email = input("Enter new email: ").strip()

    contacts[name]["phone"] = phone
    contacts[name]["email"] = email

    print("Contact updated successfully!")


def delete_contact():
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


# Main Menu
while True:
    print("\n================================")
    print("       CONTACT BOOK")
    print("================================")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice. Please try again.")