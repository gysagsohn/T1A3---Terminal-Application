#T1A3 terminal application - crearting repository

# from colored import fg, attr, bg
from truck_registry_functions import add_truck, view_truck_registry, remove_truck, update_truck_details, search_truck_classification
file_name= "registery.csv"

try:
    truck_registery_file= open(file_name, "r")
    truck_registery_file.close()
except FileNotFoundError:
    truck_registery_file = open(file_name, "w")
    truck_registery_file.write("rego,weight,classification\n")
    truck_registery_file.close()


print(f"Truck Register!")

#main page to show options
def truck_registery():
    print("1. Enter 1 add truck rego and weight to your list")
    print("2. Enter 2 to view your truck registerty")
    print("3. Enter 3 remove truck from your registry")
    print("4. Enter 4 to update truck details in registry")
    print("5. Enter 5 search for trucks based on weight classification")
    print("6. Enter 6 to exit")
    choice = input("Enter your selection: ")
    return choice

users_choice = ""

while users_choice != "6":
    users_choice = truck_registery()
    if (users_choice == "1"):
        add_truck(file_name)
    elif (users_choice == "2"):
        view_truck_registry(file_name)
    elif (users_choice == "3"):
        remove_truck(file_name)
    elif (users_choice == "4"):
        update_truck_details(file_name)
    elif (users_choice == "5"):
        search_truck_classification(file_name)
    elif (users_choice == "6"):
        continue
    else:
        print("Invalid Input")


print("Goodbye! Thank you for using the truck registery")