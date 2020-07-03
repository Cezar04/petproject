# import data_manager
import sys
import os


def menu():

    while True:
        print()
        print('''Select a number for the action that you would like to do:

    1. View the shoping list
    2. Add item in shoping list
    3. Remove item in form shoppin list
    4. Total cost
    5. Delete shoping list
    6. Exit''')
        selection = input("Make your selection: ")

        if selection == "1":
            display_list()
        elif selection == "2":
            add_item()
        elif selection == "3":
            remove_item()
        elif selection == "4":
            total_cost()
        elif selection == "5":
            delete_list()
        elif selection == "6":
            sys.exit()
        else:
            print("Invalid selection!")


price_list_copy = {}
shopping_list = price_list_copy
shopping_list = []
price_list = {}



# def add_item():
#     display_list()
#     item = input("Enter the item: ")
#     if item in shopping_list:
#         print("\n Item in shoping list!")
#     else:
#         shopping_list.append(item)
#         display_list()

def display_list():
    os.system("clear")
    print("\n***SHOPING LIST***")
    for item in shopping_list:
        print(f"# {item}")


def add_item():
    os.system("clear")
    display_list()
    user_input = input("Enter item: ")
    if user_input not in price_list:

        price_list_copy[user_input] = int(input("value?:"))
        shopping_list.append(user_input)
        display_list()
    else:
        if user_input in price_list:
            shopping_list.append(user_input)
            display_list()
                
    
def total_cost():
    os.system('clear')
    values = price_list_copy.values()
    total = sum(values)
    print(f"You have to spend {total} lei")


def remove_item():
    os.system("clear")
    display_list()
    try:
        item = input("Delete item: ")
        shopping_list.remove(item)
        price_list_copy.pop(item)
        display_list()
    except ValueError:
        print("No item to delete!")


def delete_list():
    os.system("clear")
    shopping_list.clear()
    print("Shopping list deleted!")


menu()
