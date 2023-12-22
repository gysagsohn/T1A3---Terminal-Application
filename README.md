# T1A3 - Truck Registery Application 

Link to GitHub Repository: https://github.com/gysagsohn/T1A3---Terminal-Application

Link to the presentation: TBC


# Brief submission:
I submitted the below breif for terminal application app assginement:
    I would like to make a truck register. It will keep a detail for a fleet of trucks, including key information, such as rego, model, and plant number.

    Features will include:
        to add/remove trucks
        to update the data relevant to the truck
        ability to search/sort data by any of its features
        display the register of trucks
        a feature that defines a truck based on its GVM to be LV, MV, HV

# Remote Repository
    For my remote repository I have choosen git hub. The first commite was made on 12/12


# Project managment tool
    Trello - planning to use trello to manage the process and will be added to this project submission
    Screen shot of the board on day 1 can be found at T1A3/docs/trello_board_day1
    Updated board image: 
    Finisehd project: 

# CODE STYLE CONVENTIONS:
    Pep 8 has been choosen as the style convention.

# Flow chart of my application:
Flow chart for my application has been made and it can seen under docs. 

# Function - Main page - part 1
Created main page to give user options on what they can do. Very simple number menu options: 

    ```python
    def truck_registery():
        print("1. Enter 1 to view your truck registerty")
        print("2. Enter 2 add truck rego and weight to your list")
        print("3. Enter 3 remove truck from your registry")
        print("4. Enter 4 to see weight classification of your truck")
        print("5. Enter 5 to exit")
        choice = input("Enter your selection: ")
        return choice
    ```
Considering creating a password page if I get time, but at this stage I believe this is sufficient. Will use colour function at the end. 

# Function - User choice 

Used a while loop function to define user input

    ```python
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
    ```

Each of those variable will be a function that is defined in a different page.

# Function - Add truck

I attempted using the below code for it:

    ```python
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
    ```
But it addes the user input as 1 line into the CVS folder and believe it will cause issues when I need to creat a search function and weight classification. So I changed it to:

    ```python
    def add_truck(file_name):
        print("Add truck details to register")
        truck_rego = input("Please enter truck rego: ")
        truck_weight = input("Pleas enter trucks weight in tonnes: ")
        with open(file_name, "a") as f:
            writer = csv.writer(f)
            writer.writerow([truck_rego, truck_weight])
    ```
Simple it addes the truck and weight to the CSV file in 1 line.

I thought about adding some error handling after the code was written and played around with the function. Rego should be maxed at 6 characters is the max in NSW. So I added a check for the user input can be <= to 6 characters. Also for the truck weight, I only wanted numbers and wanted to ensure that no other character was included, so I put in a float check. The code was updated to:

    ```python
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
    ```

I have also added a function called is_truck_registered to provide additional error handling if the user tries to input details of a truck that is already in the register. I basically wanted to run the check based on rego. So I created a function:

    ```python
    def is_truck_registered(file_name, truck_rego):
        #Check if a truck registration is already in the registry
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if truck_rego == row[0]:
                    return True
        return False


    # Check if the truck is already registered
    if is_truck_registered(file_name, truck_rego):
        print(f"Error: Truck with registration {truck_rego} is already in the registry.")
        return
    ```
# Function - View Truck Registry
Just needed to add a simple function to provide the user with the option to view the information they have added. Please see below for code:

    ```python
    def view_truck_registry(file_name):
        print("\nTruck Registry:")
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for truck in reader:
    ```
 
# Function - Truck weight classification
I original wanted this function to be where the user enters the rego of the truck that is already in the registry and it provides the weight clafficiation. The weight classification is if the truck weights 12T or more it is heavy vehicle (HV), if it weights 8t or less then it is a light vehicle and everything else is medium class (MV). However, as a way to demostrate that I am able to use the data input better, I have added the truck weight classification automatically so that it shows its class. The code I used to make it happen:

    ```python
    truck_classification = classify_truck_weight(truck_weight)


    writer.writerow([truck_rego, truck_weight,  truck_classification])
    ```
I nested this in the add truck function so that it shows up on the list, and the claffication is defined below:

    ```python
    def classify_truck_weight(weight):
        #Classify the weight of a truck into LV, MV, or HV
        if weight < 8:
            return "LV (Light Vehicle)"
        elif weight >= 12:
            return "HV (Heavy Vehicle)"
        else:
            return "MV (Medium Vehicle)"
    ```

Using if, elif and else to create the loop. This idea was defined in my flow digram "truck_classification_application_fuction"

Since I have made changes to the orinal plan, I have decided to change the option 4 on the main page to a different function, where a user can search for trucks based on weight classification, and it only shows those trucks when requested. Please see below for the search based on weight classification function. 

 # Function - Remove Truck from registry

 I created a function for the user to be able to remove truck from registry. I wanted the current data to display so that it was easy for the user to see what was on their list. Also, to manage handing error I wanted to add a loop where if incorrect rego was entered then the application will inform the user. 

    ```python
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
    ```

Showing the truck regsitry might not comply with DRY code principle, but I believe this would reduce user error, therefore this was inserted. 

# Function - Truck weight classification
I original wanted this function to be where the user enters the rego of the truck that is already in the registry and it provides the weight clafficiation. The weight classification is if the truck weights 12T or more it is heavy vehicle (HV), if it weights 8t or less then it is a light vehicle and everything else is medium class (MV). However, as a way to demostrate that I am able to use the data input better, I have added the truck weight classification automatically so that it shows its class. The code I used to make it happen:

    ```python
    truck_classification = classify_truck_weight(truck_weight)


    writer.writerow([truck_rego, truck_weight,  truck_classification])
    ```
I nested this in the add truck function so that it shows up on the list, and the claffication is defined below:

    ```python
    def classify_truck_weight(weight):
        #Classify the weight of a truck into LV, MV, or HV
        if weight < 8:
            return "LV (Light Vehicle)"
        elif weight >= 12:
            return "HV (Heavy Vehicle)"
        else:
            return "MV (Medium Vehicle)"
    ```

Using if, elif and else to create the loop. This idea was defined in my flow digram "truck_classification_application_fuction"

Since I have made changes to the orinal plan, I have decided to change the option 4 on the main page to a different function, where a user can search for trucks based on weight classification, and it only shows those trucks when requested. Please see below for the search based on weight classification function. 

# Function - Search based on weight classification / ordered view
I treid to make a function that would only show trucks of ceratin weight class. I could not work this out. If I have time, I will come back to this and make this function. However, I thought the second best option is once the user added the details of the truck and uses the function view truck registry, I would group them into classification and make them feature into view truck regisrty. So to make this happened I changed the view truck function to include the following code:

    ```python
    def view_truck_registry(file_name):
        print("\nTruck Registry:")
        sorted_truck_registry = sort_truck_registry(file_name)

        for truck in sorted_truck_registry:
            print(truck)

    #function to sort the order the trucks will show up in the list
    def sort_truck_registry(file_name):
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            header = next(reader)  # Skip the header row
            truck_registry = list(reader)

        # Sort the truck registry based on classification (HV, MV, LV)
        classification_order = {"HV (Heavy Vehicle)": 0, "MV (Medium Vehicle)": 1, "LV (Light Vehicle)": 2}
        sorted_truck_registry = sorted(truck_registry, key=lambda truck: classification_order.get(truck[2], 3))

        return [header] + sorted_truck_registry  # Include the header row in the sorted registry
    ```

The search function for weight classiciation is below:

    ```python
    def search_truck_classification(file_name, classification):
        # Search for trucks in the registry based on their classification
        print(f"Search for trucks with classification: {classification}")
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            trucks_found = [row for row in reader if row[2] == classification]

        if not trucks_found:
            print(f"No trucks found with classification: {classification}")
        else:
            print("\nTrucks found:")
            for truck in trucks_found:
                print(truck)
    ```

However the following error code is coming up. If I can't fix it by end of 22/12 then I will remove this from the application and work on the other things I have planned.

    ```console
    Traceback (most recent call last):
    File "/Users/gysohn/Desktop/Coder_Academy/T1A3/src/main.py", line 42, in <module>
        search_truck_classification(file_name)
    TypeError: search_truck_classification() missing 1 required positional argument: 'classification'
    ```

It is causing an error 
# Function - Update truck details
I created a function in which a user could update the details of the truck in registery if it needed to be changed, as there could be user error in inputing the details. I wanted a different solution then removing the truck and re-adding the truck again. To do this I used the following code:

```python
def update_truck_details(file_name):
    print("Update truck details in the registry")
    # Display the current truck registry so that the user knows what trucks are in their list
    view_truck_registry(file_name)

    truck_rego_to_update = input("Enter truck rego you want to update: ").upper()
    truck_registry = []

    with open(file_name, "r") as f:
        reader = csv.reader(f)
        found = False  # flag to track if the truck to update is found
        for row in reader:
            if truck_rego_to_update == row[0]:
                found = True
                print("Choose what to update:")
                print("1. Registration Number")
                print("2. Weight")
                print("3. Both")
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
                    print("Invalid choice. No updates will be made.")
                    return

                updated_classification = classify_truck_weight(updated_weight)
                truck_registry.append([updated_rego, updated_weight, updated_classification])
            else:
                truck_registry.append(row)

    if not found:
        print(f"Truck with registration number {truck_rego_to_update} not found in the registry.")
    else:
        with open(file_name, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(truck_registry)
        print(f"Truck details updated successfully.")
```

# CSV file - Truck Registry

Need a CSV file to hold the truck register informaiton. I used the code that I lernt from class. I adjusted the code to suit the truck registry from a todo list that was worked on from class. 

    ```python
    file_name= "registery.csv"

    try:
        truck_registery_file= open(file_name, "r")
        truck_registery_file.close()
    except FileNotFoundError:
        truck_registery_file = open(file_name, "w")
        truck_registery_file.write("rego,weight\n")
        truck_registery_file.close()
    ```
Further used error function if file could not be found based on what I learned during class. As of 18/12 this has not been tested, and might be updated as I develop the app. 

# Python Packages
I have choosen to import the following packages:
- colored 
- numpy 
- pandas 
- requests 
- matplotlib
- os

Colored is the main function that I intend to use in my application. As the application developes I intend to use the others. 

# Instruction manual

1. Dowload git gub represitory
2. ls -l
3. chmod +x run.sh
4. ./run.sh
5. deactivate


# Reference List
    - van Rossum, G, Warsaw, B & Coghlan, N 2001, PEP 8 – Style Guide for Python Code | peps.python.org, viewed 15/12/23 <peps.python.org>
    -‌ GeeksforGeeks 2019, GeeksforGeeks | A computer science portal for geeks, viewed 15/12/23 <GeeksforGeeks.>‌
    W3Schools 2019, Python Tutorial, viewed 15/12/23 <W3schools.com>
    -‌ LAB, V n.d., colour: converts and manipulates various color representation (HSL, RVB, web, X11, ...), PyPI viewed 16/12/23 <c​https://pypi.org/project/colour/>
‌
