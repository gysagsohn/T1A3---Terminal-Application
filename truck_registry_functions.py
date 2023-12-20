import csv


def add_truck(file_name):
    print("Add truck details to register")
# user input for truck rego and error handling if the rego is longer then 6 characters
    while True:
        truck_rego = input("Please enter truck rego (max 6 characters): ").upper()
        if len(truck_rego) <= 6:
            break
        else:
            print("Invalid input. The truck registration number must be exactly 6 characters.")
    # user input to get truck weight
    truck_weight = get_valid_float_input("Please enter truck's weight in tonnes(numbers only): ")
    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([truck_rego, truck_weight])
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
 

