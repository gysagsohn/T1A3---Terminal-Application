

def view_truck (file_name):
    print("View truck list!")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            # row = ["Truck 1", "False"]
            if (row[1] == "True"):
                print(f"Todo {row[0]} is complete")
            else:
                print(f"Todo {row[0]} is not complete")