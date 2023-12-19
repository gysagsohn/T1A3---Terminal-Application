import csv

def add_truck(file_name):
    print("Add truck to your registry")
    
    while True:
        print("Type 'stop' to finish")
        truck_rego = input("Enter the truck rego: ").upper
        truck_make = input("Enter the truck make: ").upper
        truck_weight = input("Enter the truck weight(in tonne only):")
        if truck_rego.lower() == 'stop':
            break  # exit the loop if the user types 'stop'
        
        # Open file - list.csv
        with open(file_name, "a") as f:
            writer = csv.writer(f)
            writer.writerow([truck_rego, truck_make, truck_weight])

# Example usage
add_truck("your_file.csv")