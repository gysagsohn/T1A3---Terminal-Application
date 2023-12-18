#T1A3 terminal application - crearting repository

# from colored import fg, attr, bg

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
    users_choice = create_registerty()
    if (users_choice == "1"):
        view_truck(file_name)
    elif (users_choice == "2"):
        add_truck(file_name)
    elif (users_choice == "3"):
        remove_truck(file_name)
    elif (users_choice == "4"):
        weight_classification_truck(file_name)
    elif (users_choice == "5"):
        continue
    else:
        print("Invalid Input")


print("Goodbye! Thank you for using the truck registery")