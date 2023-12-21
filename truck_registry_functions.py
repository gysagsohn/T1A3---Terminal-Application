import csv

def is_truck_registered(file_name, truck_rego):
    #Check if a truck registration is already in the registry
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if truck_rego == row[0]:
                return True
    return False

def add_truck(file_name):
    print("Add truck details to register")
    # user input for truck rego and error handling if the rego is longer then 6 characters
    while True:
        truck_rego = input("Please enter truck rego (max 6 characters): ").upper()
        if len(truck_rego) <= 6:
            break
        else:
            print("Invalid input. The truck registration can be 6 characters or less.")
    # Check if the truck is already registered
    if is_truck_registered(file_name, truck_rego):
        print(f"Error: Truck with rego {truck_rego} is already in the registry.")
        return
    # user input to get truck weight
    truck_weight = get_valid_float_input("Please enter truck's weight in tonnes(numbers only): ")
    #adding function for truck classification
    truck_classification = classify_truck_weight(truck_weight)
    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([truck_rego, truck_weight,  truck_classification])
#error fixing if the weight of truck is not numbers
def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter numbers only.")



def view_truck_registry(file_name):
    print("\nTruck Registry:")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for truck in reader:
            print(truck)
 
def classify_truck_weight(weight):
    #Classify the weight of a truck into LV, MV, or HV
    if weight < 8:
        return "LV (Light Vehicle)"
    elif weight >= 12:
        return "HV (Heavy Vehicle)"
    else:
        return "MV (Medium Vehicle)"

def remove_truck(file_name):
    print("Remove truck from registry")
    # Display the current truck registry so that user knows what truck is in their list
    print("Current Truck Registry:")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    truck_rego_to_remove = input("Enter truck rego you want to remove: ").upper()
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
            print(f"Truck with registration number {truck_rego_to_remove} not found in the registry.")
    with open(file_name, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(truck_rego)