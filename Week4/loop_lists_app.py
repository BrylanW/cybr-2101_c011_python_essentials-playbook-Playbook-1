#loop_lists_app.py
# A simple program that uses loops and lists to gather user input and display it.
#Author: Brylan Williamson
print("Welcome to the loop and lists app!")
# Displays a welcome message to the user
# Create an empty list to store items
items = []

# Define a variable to control the main menu loop
running = True

# Start the menu loop
while running:
    # Display the main menu options
    print("===== SIMPLE LIST MENU =====")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View all items")
    print("4. Exit")
    
    # Ask for the user's choice
    choice = input("Enter your choice (1-4): ")

    # Check what the user entered
    if choice == "1":
        # Add an item
        new_item = input("Enter the item to add: ").strip()
        if new_item:  # Make sure it's not empty
            items.append(new_item)
            print(f"'{new_item}' added to the list.")
        else:
            print("Item cannot be empty.")

    elif choice == "2":
        # Remove an item
        if len(items) == 0:
            print("The list is empty. Nothing to remove.")
        else:
            remove_item = input("Enter the item to remove: ").strip()
            if remove_item in items:
                items.remove(remove_item)
                print(f"'{remove_item}' removed from the list.")
            else:
                print(f"'{remove_item}' not found in the list.")

    elif choice == "3":
        # Display all items in the list
        if len(items) == 0:
            print("The list is currently empty.")
        else:
            print("\nCurrent list items:")
            # Use a for loop to print each item with its number
            for index, item in enumerate(items, start=1):
                print(f"{index}. {item}")

    elif choice == "4":
        # Exit the program
        print("Exiting program. Goodbye!")
        running = False

    else:
        # Input validation for wrong choices
        print("Invalid choice. Please enter a number between 1 and 4.")
