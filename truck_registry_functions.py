import csv


def add_truck(file_name):
    print("Add truck details to register")
    truck_rego = input("Please enter truck rego: ")
    truck_weight = input("Pleas enter trucks weight in tonnes: ")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([truck_rego, truck_weight])

        