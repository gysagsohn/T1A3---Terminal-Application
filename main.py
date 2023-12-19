#T1A3 terminal application - crearting repository

# from colored import fg, attr, bg
from truck_registry_functions import add_truck

file_name= "registery.csv"

try:
    truck_registery_file= open(file_name, "r")
    truck_registery_file.close()
    print("In try block")
except FileNotFoundError:
    truck_registery_file = open(file_name, "w")
    truck_registery_file.write("title,completed\n")
    truck_registery_file.close()
    print("In except block")


print(f"Truck Register!")

#main page to show options
def truck_registery():
    print("1. Enter 1 to view your truck registerty")
    print("2. Enter 2 add truck rego and weight to your list")
    print("3. Enter 3 remove truck from your registry")
    print("4. Enter 4 to see weight classification of your truck")
    print("5. Enter 5 to exit")
    choice = input("Enter your selection: ")
    return choice

users_choice = ""

while users_choice != "5":
    users_choice = truck_registery()
    if (users_choice == "1"):
        add_truck(file_name)
    elif (users_choice == "2"):
        view_truck(file_name)
        pass
    elif (users_choice == "3"):
        remove_truck(file_name)
        pass
    elif (users_choice == "4"):
        pass
        weight_classification_truck(file_name)
    elif (users_choice == "5"):
        continue
    else:
        print("Invalid Input")


print("Goodbye! Thank you for using the truck registery")