# -------------------------------------------------------------
# Community Food Pantry Inventory Tracker
# Author: Brylan Williamson
#
# Description:
#   A structured program that manages a community food pantry.
#   Features:
#       - Menu driven interface
#       - Add, remove, and view inventory items
#       - Structured storage using dictionaries + nested dictionaries
#       - Input validation and error handling
#       - File handling to save/load inventory data automatically
# -------------------------------------------------------------

import json
import os

print("Welcome to the Community Food Pantry Inventory Tracker!")

# Inventory format:
# { item_name: {"qty": int, "category": string} }
inventory = {}

# Allowed categories
CATEGORIES = ("Canned", "Fresh", "Dry Goods")

# File where inventory is stored
DATA_FILE = "pantry_inventory.json"


# -------------------------------------------------------------
# File I/O Functions
# -------------------------------------------------------------
def load_inventory():
    """Load inventory from a JSON file if it exists."""
    global inventory

    if not os.path.exists(DATA_FILE):
        print("No saved inventory found. Starting fresh.")
        return

    try:
        with open(DATA_FILE, "r") as file:
            inventory = json.load(file)
        print("Inventory loaded successfully.")
    except (json.JSONDecodeError, IOError):
        print("Error loading inventory file. Starting with an empty inventory.")
        inventory = {}


def save_inventory():
    """Save inventory to a JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(inventory, file, indent=4)
        print("Inventory saved successfully.")
    except IOError:
        print("Error: Could not save the inventory.")


# -------------------------------------------------------------
# Menu Display
# -------------------------------------------------------------
def display_menu():
    """Print the pantry menu options."""
    print("\n--- Community Food Pantry Inventory Tracker ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Inventory")
    print("4. Exit")


# -------------------------------------------------------------
# Inventory Operations
# -------------------------------------------------------------
def add_item():
    """Add an item to the inventory with error handling."""
    print("\n--- Add Item ---")

    item = input("Enter item name: ").strip().title()
    if not item:
        print("Item name cannot be empty.")
        return

    # Get quantity
    try:
        quantity = int(input("Enter quantity to add: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            return
    except ValueError:
        print("Invalid number. Please enter a valid quantity.")
        return

    # Display category options
    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"{i}. {cat}")

    # Choose category
    try:
        choice = int(input("Choose a category (number): "))
        if choice < 1 or choice > len(CATEGORIES):
            print("Invalid category selected.")
            return
        category = CATEGORIES[choice - 1]
    except ValueError:
        print("Invalid input. Must be a number.")
        return

    # Update inventory
    if item in inventory:
        inventory[item]["qty"] += quantity
    else:
        inventory[item] = {"qty": quantity, "category": category}

    print(f"{item} added. Total Quantity: {inventory[item]['qty']} "
          f"(Category: {category})")


def remove_item():
    """Remove or decrease quantity of an existing item."""
    print("\n--- Remove Item ---")

    item = input("Enter item name to remove: ").strip().title()

    if item not in inventory:
        print("Item not found in inventory.")
        return

    # Remove quantity
    try:
        quantity = int(input("Enter quantity to remove: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            return
    except ValueError:
        print("Invalid number.")
        return

    inventory[item]["qty"] -= quantity

    # Remove item completely when qty reaches 0
    if inventory[item]["qty"] <= 0:
        del inventory[item]
        print(f"{item} has been removed completely from inventory.")
    else:
        print(f"{item} now has {inventory[item]['qty']} left.")


def view_inventory():
    """Display all inventory items."""
    print("\n--- Current Inventory ---")

    if not inventory:
        print("Inventory is empty.")
        return

    for item, info in inventory.items():
        print(f"{item} - Quantity: {info['qty']} | Category: {info['category']}")


# -------------------------------------------------------------
# Main Program Loop
# -------------------------------------------------------------
def main():
    """Main loop of the program."""
    load_inventory()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            print("Saving data...")
            save_inventory()
            print("Thank you for using the Food Pantry Tracker. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1–4.")


# Run the main program
main()
