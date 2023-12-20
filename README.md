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

# Main page - function 1 part 1 and user input 1w
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

# Users Choice - fuction 1 part 2

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

# Add truck function

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
# Function - View Truck Registry
Just needed to add a simple function to provide the user with the option to view the information they have added. Please see below for code:

    ```python
    def view_truck_registry(file_name):
        print("\nTruck Registry:")
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for truck in reader:
    ```
 I want this to be a separate function where a user can see the weight classification if they ask the program, but I am not sure how I can do that. I will see if I can come up with a solution to do that. If not I will need to add this to add truck function so that it addes it directly to the CSV file as the third input and can be viewed when the user selects view registry function. 
 
 I will come back to this as the git remove should be easy enough

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

**# CSV file for truck registry 

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

# Reference List
    - van Rossum, G, Warsaw, B & Coghlan, N 2001, PEP 8 – Style Guide for Python Code | peps.python.org, viewed 15/12/23 <peps.python.org>
    -‌ GeeksforGeeks 2019, GeeksforGeeks | A computer science portal for geeks, viewed 15/12/23 <GeeksforGeeks.>‌
    W3Schools 2019, Python Tutorial, viewed 15/12/23 <W3schools.com>
    -‌ LAB, V n.d., colour: converts and manipulates various color representation (HSL, RVB, web, X11, ...), PyPI viewed 16/12/23 <c​https://pypi.org/project/colour/>
‌
