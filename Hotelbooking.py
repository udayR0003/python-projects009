# ==========================================
# HOTEL BOOKING MANAGEMENT SYSTEM
# ==========================================

rooms = {
    101: {"type": "Single", "price": 1500, "status": "Available"},
    102: {"type": "Single", "price": 1500, "status": "Available"},
    103: {"type": "Double", "price": 2500, "status": "Available"},
    104: {"type": "Double", "price": 2500, "status": "Available"},
    105: {"type": "Deluxe", "price": 4000, "status": "Available"}
}

bookings = {}


def show_rooms():
    print("\n========== ROOM LIST ==========")

    for room_no, room in rooms.items():
        print(
            f"Room: {room_no} | "
            f"Type: {room['type']} | "
            f"Price: ₹{room['price']} | "
            f"Status: {room['status']}"
        )


def book_room():
    show_rooms()

    try:
        room_no = int(input("\nEnter room number: "))

        if room_no not in rooms:
            print("Room does not exist.")
            return

        if rooms[room_no]["status"] == "Booked":
            print("Room is already booked.")
            return

        name = input("Enter guest name: ")
        phone = input("Enter phone number: ")
        days = int(input("Enter number of days: "))

        if days <= 0:
            print("Number of days must be greater than 0.")
            return

        total = rooms[room_no]["price"] * days

        bookings[room_no] = {
            "name": name,
            "phone": phone,
            "days": days,
            "total": total
        }

        rooms[room_no]["status"] = "Booked"

        print("\nBooking successful!")
        print("Guest Name:", name)
        print("Room Number:", room_no)
        print("Total Amount: ₹", total)

    except ValueError:
        print("Please enter a valid number.")


def view_bookings():
    print("\n========== CURRENT BOOKINGS ==========")

    if not bookings:
        print("No bookings found.")
        return

    for room_no, booking in bookings.items():
        print("\nRoom Number:", room_no)
        print("Guest Name:", booking["name"])
        print("Phone:", booking["phone"])
        print("Days:", booking["days"])
        print("Total: ₹", booking["total"])


def checkout():
    try:
        room_no = int(input("Enter room number for checkout: "))

        if room_no not in bookings:
            print("No booking found for this room.")
            return

        guest = bookings[room_no]["name"]

        del bookings[room_no]
        rooms[room_no]["status"] = "Available"

        print(f"{guest} checked out successfully.")
        print(f"Room {room_no} is now available.")

    except ValueError:
        print("Please enter a valid room number.")


# Main Menu
while True:
    print("\n================================")
    print("   HOTEL BOOKING SYSTEM")
    print("================================")
    print("1. Show Rooms")
    print("2. Book Room")
    print("3. View Bookings")
    print("4. Checkout")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_rooms()

    elif choice == "2":
        book_room()

    elif choice == "3":
        view_bookings()

    elif choice == "4":
        checkout()

    elif choice == "5":
        print("Thank you for using Hotel Booking System!")
        break

    else:
        print("Invalid choice. Please try again.")
