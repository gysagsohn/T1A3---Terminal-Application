import csv
from function_colors import invalid_error_color, user_selection_color, header_function_colour, option, truck_rego_color, option, truck_rego_color,truck_classification_color, truck_weight_color, reset

def is_truck_registered(file_name, truck_rego):
    #Check if a truck registration is already in the registry
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if truck_rego == row[0]:
                return True
    return False

def add_truck(file_name):
    print(f"{header_function_colour}Add truck details to register{reset}")
    # user input for truck rego and error handling if the rego is longer then 6 characters
    while True:
        truck_rego = input(f"{user_selection_color}Please enter truck rego (max 6 characters): {reset}").upper()
        if len(truck_rego) <= 6:
            break
        else:
            print(f"{invalid_error_color}Invalid input. The truck registration can be 6 characters or less.{reset}")
    # Check if the truck is already registered
    if is_truck_registered(file_name, truck_rego):
        print(f"{invalid_error_color}Error: Truck with rego {truck_rego} is already in the registry.{reset}")
        return
    # user input to get truck weight
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 1238ba9 (colored pythong package code update)
    truck_weight = get_valid_float_input(f"{user_selection_color}Please enter truck's weight in tonnes(numbers only): {reset}")
    #adding function for truck classification
    truck_classification = classify_truck_weight(truck_weight)
    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([truck_rego, truck_weight, truck_classification])
<<<<<<< HEAD
=======
    truck_weight = get_valid_float_input("Please enter truck's weight in tonnes(numbers only): ")
    truck_classification = classify_truck_weight(truck_weight)
    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([truck_rego, truck_weight,  truck_classification])
>>>>>>> cd3212c (Add function classify truck weight)
=======
>>>>>>> 8a82092 (add function to update truck details in registry and order the truck list)
#error fixing if the weight of truck is not numbers
def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print(f"{user_selection_color}Invalid input. Please enter numbers only.{reset}")



def view_truck_registry(file_name):
<<<<<<< HEAD
<<<<<<< HEAD
    print(f"{header_function_colour}\nTruck Registry:{reset}")
    sorted_truck_registry = sort_truck_registry(file_name)

    for truck in sorted_truck_registry:
        formatted_truck = f"{truck_rego_color}{truck[0]}{reset}, {truck_weight_color}{truck[1]}{reset}, {truck_classification_color}{truck[2]}{reset}"
        print(formatted_truck)


=======
    print("\nTruck Registry:")
    sorted_truck_registry = sort_truck_registry(file_name)

    for truck in sorted_truck_registry:
        print(truck)
>>>>>>> 8a82092 (add function to update truck details in registry and order the truck list)
=======
    print(f"{header_function_colour}\nTruck Registry:{reset}")
    sorted_truck_registry = sort_truck_registry(file_name)

    for truck in sorted_truck_registry:
        formatted_truck = f"{truck_rego_color}{truck[0]}{reset}, {truck_weight_color}{truck[1]}{reset}, {truck_classification_color}{truck[2]}{reset}"
        print(formatted_truck)


>>>>>>> 1238ba9 (colored pythong package code update)

#function to sort the order the trucks will show up in the list
def sort_truck_registry(file_name):
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip the header row
        truck_registry = list(reader)

    # Sort the truck registry based on classification (HV, MV, LV)
<<<<<<< HEAD
    classification_order = {"HV (Heavy Vehicle)": 0, "MV (Medium Vehicle)": 1, "LV (Light Vehicle)": 2}
    sorted_truck_registry = sorted(truck_registry, key=lambda truck: classification_order.get(truck[2], 3))
=======
    sorted_truck_registry = sorted(truck_registry, key=lambda truck: truck[2])
>>>>>>> 8a82092 (add function to update truck details in registry and order the truck list)

    return [header] + sorted_truck_registry  # Include the header row in the sorted registry

 
def classify_truck_weight(weight):
    #Classify the weight of a truck into LV, MV, or HV
    if weight < 8:
        return "LV (Light Vehicle)"
    elif weight >= 12:
        return "HV (Heavy Vehicle)"
    else:
        return "MV (Medium Vehicle)"

def remove_truck(file_name):
    print(f"{header_function_colour}Remove truck from registry{reset}")
    # Display the current truck registry so that user knows what truck is in their list
    print(f"{header_function_colour}Current Truck Registry:{reset}")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    truck_rego_to_remove = input(f"{user_selection_color}Enter truck rego you want to remove: {reset}").upper()
    truck_rego = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        found = False  # flag to track if the truck to remove is found
        for row in reader:
            if truck_rego_to_remove == row[0]:
                found = True
            else:
                truck_rego.append(row)
        # error handling if a truck rego that is not on the list has been entered
        if not found:
            print(f"{user_selection_color}Truck with registration number {truck_rego_to_remove} not found in the registry.{reset}")
    with open(file_name, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(truck_rego)


def update_truck_details(file_name):
<<<<<<< HEAD
<<<<<<< HEAD
    print(f"{header_function_colour}Update truck details in the registry{reset}")
    # Display the current truck registry so that the user knows what trucks are in their list
    view_truck_registry(file_name)

    truck_rego_to_update = input(f"{user_selection_color}Enter truck rego you want to update: {reset}").upper()
=======
    print("Update truck details in the registry")
    # Display the current truck registry so that the user knows what trucks are in their list
    view_truck_registry(file_name)

    truck_rego_to_update = input("Enter truck rego you want to update: ").upper()
>>>>>>> 8a82092 (add function to update truck details in registry and order the truck list)
=======
    print(f"{header_function_colour}Update truck details in the registry{reset}")
    # Display the current truck registry so that the user knows what trucks are in their list
    view_truck_registry(file_name)

    truck_rego_to_update = input(f"{user_selection_color}Enter truck rego you want to update: {reset}").upper()
>>>>>>> 1238ba9 (colored pythong package code update)
    truck_registry = []

    with open(file_name, "r") as f:
        reader = csv.reader(f)
        found = False  # flag to track if the truck to update is found
        for row in reader:
            if truck_rego_to_update == row[0]:
                found = True
<<<<<<< HEAD
<<<<<<< HEAD
                print(f"{option}Choose what to update:")
                print("1. Registration Number")
                print("2. Weight")
                print("3. Both('reset')")
=======
                print("Choose what to update:")
                print("1. Registration Number")
                print("2. Weight")
                print("3. Both")
>>>>>>> 8a82092 (add function to update truck details in registry and order the truck list)
=======
                print(f"{option}Choose what to update:")
                print("1. Registration Number")
                print("2. Weight")
                print("3. Both('reset')")
>>>>>>> 1238ba9 (colored pythong package code update)
                choice = input("Enter your choice (1, 2, or 3): ")
                if choice == "1":
                    updated_rego = input("Enter the new registration number: ").upper()
                    updated_weight = row[1]  # Keep the existing weight
                elif choice == "2":
                    updated_rego = row[0]  # Keep the existing registration number
                    updated_weight = get_valid_float_input("Enter the new weight in tonnes (numbers only): ")
                elif choice == "3":
                    updated_rego = input("Enter the new registration number: ").upper()
                    updated_weight = get_valid_float_input("Enter the new weight in tonnes (numbers only): ")
                else:
<<<<<<< HEAD
<<<<<<< HEAD
                    print(f"{invalid_error_color}Invalid choice. No updates will be made.{reset}")
=======
                    print("Invalid choice. No updates will be made.")
>>>>>>> 8a82092 (add function to update truck details in registry and order the truck list)
=======
                    print(f"{invalid_error_color}Invalid choice. No updates will be made.{reset}")
>>>>>>> 1238ba9 (colored pythong package code update)
                    return
                updated_classification = classify_truck_weight(updated_weight)
                truck_registry.append([updated_rego, updated_weight, updated_classification])
            else:
                truck_registry.append(row)
    if not found:
<<<<<<< HEAD
<<<<<<< HEAD
        print(f"{invalid_error_color}Truck with registration number {truck_rego_to_update} not found in the registry.{reset}")
=======
        print(f"Truck with registration number {truck_rego_to_update} not found in the registry.")
>>>>>>> 8a82092 (add function to update truck details in registry and order the truck list)
=======
        print(f"{invalid_error_color}Truck with registration number {truck_rego_to_update} not found in the registry.{reset}")
>>>>>>> 1238ba9 (colored pythong package code update)
    else:
        with open(file_name, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(truck_registry)
<<<<<<< HEAD
<<<<<<< HEAD
        print(f"{header_function_colour}Truck details updated successfully.{reset}")

def search_truck_classification(file_name, classification):
    # Search for trucks in the registry based on their classification
    print(f"{header_function_colour}Search for trucks with classification: {classification}{reset}")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        trucks_found = [row for row in reader if row[2] == classification]

    if not trucks_found:
        print(f"{header_function_colour}No trucks found with classification: {classification}{reset}")
    else:
        print(f"{header_function_colour}\nTrucks found:{reset}")
        for truck in trucks_found:
            print(truck)
=======
=======
>>>>>>> 1238ba9 (colored pythong package code update)
        print(f"Truck details updated successfully.")
<<<<<<< HEAD
>>>>>>> 8a82092 (add function to update truck details in registry and order the truck list)
=======
<<<<<<< HEAD
=======
=======
        print(f"{header_function_colour}Truck details updated successfully.{reset}")
>>>>>>> 138cd7a (colored pythong package code update)

def search_truck_classification(file_name, classification):
    # Search for trucks in the registry based on their classification
    print(f"{header_function_colour}Search for trucks with classification: {classification}{reset}")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        trucks_found = [row for row in reader if row[2] == classification]

    if not trucks_found:
        print(f"{header_function_colour}No trucks found with classification: {classification}{reset}")
    else:
        print(f"{header_function_colour}\nTrucks found:{reset}")
        for truck in trucks_found:
            print(truck)
>>>>>>> 9dd5a0a (Added serach function for weight but causes error. Need more work)
>>>>>>> 595c5f8 (Added serach function for weight but causes error. Need more work)
