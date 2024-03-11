'''
4. The Shopping List Maker
Objective:
The aim of this assignment is to create a program that helps users make a shopping list.

Task 1: Write a function that lets the user add items to a list.
Task 2: Include a feature to remove items from the list.
Task 3: Add a function that prints out the entire list in a formatted way.
'''

products = ['Boots', 'Sandals', 'Heels', 'Sneakers', 'Flats', 'Flip Flops']

def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Inventory")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            new_item = input("Enter the name of the new product: ")
            products.append(new_item)
            print(f"{new_item} has been added to the inventory!")
        elif choice == "2":
            remove_item = input("Enter the name of the product to be removed: ")
            products.append(remove_item)
            print(f"{remove_item} has been removed from the inventory!")
        elif choice == "3":
            print("\nCurrnet Inventory: ")
            for product in products[:5]:
                print(product)
            if len(products) > 5:
                print(".... loading more!")
        elif choice == "4":
            print("Exiting System")
            break
        else:
            print("Invalid selection, please try again.")
manage_inventory()
