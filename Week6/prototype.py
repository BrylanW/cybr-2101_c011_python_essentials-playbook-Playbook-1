# -------------------------------------------------------------
# Community Food Pantry Inventory Tracker
# Author: Brylan Williamson
# Description:
#   A structured version of the original program using
#   functions, tuples, dictionaries, error handling,
#   and a clean menu driven design.
# -------------------------------------------------------------

print("Welcome to the Community Food Pantry Inventory Tracker!")

# Inventory structure: { item_name: {"qty": number, "category": category_string} }
inventory = {}

# allowed categories
CATEGORIES = ("Canned", "Fresh", "Dry Goods")


def display_menu():
    """Print the pantry menu options."""
    print("\n--- Community Food Pantry Inventory Tracker ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Inventory")
    print("4. Exit")


def add_item():
    """Add an item to the inventory with error handling."""
    print("\n--- Add Item ---")

    item = input("Enter item name: ").strip()

    # Get quantity safely
    try:
        quantity = int(input("Enter quantity to add: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            return
    except ValueError:
        print("Invalid number. Please enter a valid quantity.")
        return

    # Choose a category for the item
    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"{i}. {cat}")

    try:
        cat_choice = int(input("Choose a category (number): "))
        if cat_choice < 1 or cat_choice > len(CATEGORIES):
            print("Invalid category selected.")
            return
        category = CATEGORIES[cat_choice - 1]
    except ValueError:
        print("Invalid input. Must be a number.")
        return

    # Update inventory
    if item in inventory:
        inventory[item]["qty"] += quantity
    else:
        inventory[item] = {"qty": quantity, "category": category}

    print(f"{item} added. Total Quantity: {inventory[item]['qty']} (Category: {category})")


def remove_item():
    """Remove or decrease quantity of an existing item."""
    print("\n--- Remove Item ---")

    item = input("Enter item name to remove: ").strip()

    if item not in inventory:
        print("Item not found in inventory.")
        return

    try:
        quantity = int(input("Enter quantity to remove: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            return
    except ValueError:
        print("Invalid number.")
        return

    inventory[item]["qty"] -= quantity

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


def main():
    """Main loop of the program."""
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
            print("Thank you for using the Food Pantry Tracker. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1–4.")


# Run the main program
main()
