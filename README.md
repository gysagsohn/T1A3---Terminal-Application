## T1A3 - Truck Registers Application 

Link to GitHub Repository: https://github.com/gysagsohn/T1A3---Terminal-Application

Link to the presentation: https://youtu.be/JK5F8Wg_DD8

# Requirements for application

- Device - need any device that supports python, including desktop, laptop, screen, keyboard and mouse
- Command line interface
- Python >=3
- Operating System - The application is platform independent and can run on various operating systems, including Windows, macOS, and Linux.
- Internet Connection - Internet connection is required to download the required packages. If already installed then it might not be required 
- Ram 2GB
- 1 GB free disk space

# Installation Steps
**Step 1 Download Repository**

Visit the GitHub repository for the T1A3--Truck-Registry-Application:

https://github.com/gysagsohn/T1A3---Terminal-Application

Click on the "Code" button and choose "Download ZIP" to download the repository as a ZIP file.

**Step 2 Unzip file**

Locate the downloaded file and extract the file. Right click on the ZIP file and select "Extract ALL" and/or use an unzip tool. 


**Step 3 Open a Terminal or Command Prompt**

Depending on your operating system, open a terminal or command prompt:

- Windows: Press Win + R, type cmd, and press Enter.
- macOS: Press Cmd + Space, type Terminal, and press Enter.
- Linux: Press Ctrl + Alt + T or use your preferred terminal application.

**Step 4: Navigate to the Application Folder**

Use cd command in terminal or command prompt to to navigate to the folder where you extracted the application. For example:

```bash
    
    cd /path/to/T1A3--Truck-Registry-Application
    
```

**Step 4 Software requirement** - optional 

Python 3 or above is required for this system. If you are unsure if you have this programme, just skip this step and go to next step. 

If you wish to check that if you have Python 3, please run python3_check.sh. Please use the following command:

```bash

    chmod +x check_python3.sh #Save the file and make it executable

    ./check_python3.sh #run script

```

If you don't please follow the below guide on how to install Python 3:

https://www.python.org/downloads/

Please note you do not required to do this as Step 7 will check if you have Python 3 as well.

**Step 6 check for internect connection** - optional 

Internet connection is required to download the required packages. If already installed then it might not be required.

If you wish to check if you have internet, please run internet_connection_check.sh Please use the following command:

```bash

    chmod +x internet_connection_check.sh #Save the file and make it executable

    ./internet_connection_check.sh  #run script

```

**Step 7: Run the Installation Script to Run Programme**

Run the  installation script (run.sh) by executing the following commands:

```bash
    ```
    chmod +x install.sh  # Make the script executable (macOS and Linux only)
    ./run.sh         # Run the installation script
   ```
This script will check if Python 3 is installed, create a virtual environment, install necessary dependencies, and activate the virtual environment and open the application. If Python 3 is not installed, please return to step 3 and following the instruction manual.

Following dependencies are used
- colored 
- numpy 
- pandas 
- requests 
- matplotlib

Currently only colored is being used, but for future versions the others will be required. 

If the application does not open, please follow Step 7

**Step 7A: Run Application** - optional

Once the script is completed, please type the following to you terminal and/or command:

```python
    python3 main.py
```
This step shouln't be required as the script contains the command to run the application 

# How to use

The instructions on what to do are provided with each input. However, the first function will look like this 

Images/termal_application_main_page.png

Use your keyboard to write in the relevant user input as requested by the program. 

# Brief submission:
I submitted the below brief for terminal application app assignment: I would like to make a truck register. It will keep a detail for a fleet of trucks, including key information, such as rego, model, and plant number.

    Features will include:
        to add/remove trucks
        to update the data relevant to the truck
        ability to search/sort data by any of its features
        display the register of trucks
        a feature that defines a truck based on its GVM to be LV, MV, HV

# Remote Repository
For my remote repository I have chosen git hub. The first commit was made on 12/12

# Project management tool
Trello - planning to use trello to manage the process and will be added to this project submission
Screen shot of the board on 

Images/Trello_board_day1.png

Images/Trello_board_day2.png

Images/Trello_board_day3.png

Images/Trello_board_day4.png

Images/Trello_board_day5.png

Images/Trello_board_day6.png

Images/Trello_board_day7.png

Images/Trello_board_day8.png

Images/Trello_board_day9.png

Images/trello_board_lastday.png

# CODE STYLE CONVENTIONS:
Pep 8 has been chosen as the style convention.

I wasn't able to maintain the max 72 charater per line requirement. I will work on this for next project

# Flow chart of my application:
Flow chart for my application has been made and it can seen under docs. 

Images/Truck Registerty.drawio.png

Images/truck_classification_application_fuction.drawio.png

# Function - Main page - part 1
Created main page to give user options on what they can do. Very simple number menu options: 

```python

    #main page to show options
    def truck_registry():
        print(f"{fg('green')}1. Enter 1 add truck rego and weight to your list {attr('reset')}")
        print(f"{fg('green')}2. Enter 2 to view your truck registry {attr('reset')}")
        print(f"{fg('green')}3. Enter 3 remove truck from your registry {attr('reset')}")
        print(f"{fg('green')}4. Enter 4 to update truck details in registry {attr('reset')}")
        print(f"{fg('green')}5. Enter 5 to exit {attr('reset')}")
        choice = input(f"{fg('yellow')}Enter your selection: {attr('reset')}")
        return choice

```
Considering creating a password page if I get time, but at this stage I believe this is sufficient. Will use colour function at the end. 

After adding the color import:

```python

    #main page to show options
    def truck_registry():
        print(f"{fg('green')}1. Enter 1 add truck rego and weight to your list")
        print("2. Enter 2 to view your truck registry")
        print("3. Enter 3 remove truck from your registry")
        print("4. Enter 4 to update truck details in registry")
        print("5. Enter 5 search for trucks based on weight classification")
        print("6. Enter 6 to exit ('reset')}")
        choice = input(f"{fg('yellow')}Enter your selection: {attr('reset')}")
        return choice

```


# Function - User choice 

Used a while loop function to define user input

```python

    users_choice = ""


    while users_choice != "6":
        users_choice = truck_registry()
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
        print(f"{fg('red')}{attr('bold')}Invalid Input{attr('reset')}")
        
```

After adding the color import:

```python

    while users_choice != "6":
        users_choice = truck_registry()
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
        print(f"{fg('red')}{attr('bold')}Invalid Input{attr('reset')}")

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
But it adds the user input as 1 line into the CVS folder and believe it will cause issues when I need to create a search function and weight classification. So I changed it to:

```python
    try:
        truck_registry_file= open(file_name, "r")
        truck_registry_file.close()
    except FileNotFoundError:
        truck_registry_file = open(file_name, "w")
        truck_registry_file.write("rego,weight,classification\n")
        truck_registry_file.close()
```
It simply adds the rego, weight and classification to the CSV file in 1 line.

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

After adding the color function the final code is:

```python

    def add_truck(file_name):
        print(f"{header_function_colour}Add truck details to register{reset}")
        # User input for truck rego and error handling if the rego is longer than 6 characters
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
        
        # User input to get truck weight
        truck_weight = get_valid_float_input(f"{user_selection_color}Please enter truck's weight in tonnes(numbers only): {reset}")
        # Adding function for truck classification
        truck_classification = classify_truck_weight(truck_weight)
        with open(file_name, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([truck_rego, 
                            truck_weight,
                            truck_classification])
                            
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

After adding the color import:

```python

    # Function to show the truck registry 
    def view_truck_registry(file_name):
        print(f"{header_function_colour}\nTruck Registry:{reset}")
        sorted_truck_registry = sort_truck_registry(file_name)

        for truck in sorted_truck_registry:
            formatted_truck = f"{truck_rego_color}{truck[0]}{reset}, {truck_weight_color}{truck[1]}{reset}, {truck_classification_color}{truck[2]}{reset}"
            print(formatted_truck)

```
 
# Function - Truck weight classification
I original wanted this function to be where the user enters the rego of the truck that is already in the registry and it provides the weight classification. The weight classification is if the truck weights 12T or more it is heavy vehicle (HV), if it weights 8t or less then it is a light vehicle and everything else is medium class (MV). However, as a way to demonstrate that I am able to use the data input, I have added the truck weight classification automatically so that it shows its class. The code I used to make it happen:

```python

    truck_classification = classify_truck_weight(truck_weight)


    writer.writerow([truck_rego, truck_weight, truck_classification])

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

Since I have made changes to the original plan, I have decided to change the option 4 on the main page to a different function, where a user can search for trucks based on weight classification, and it only shows those trucks when requested. Please see below for the search based on weight classification function. 

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

Showing the truck registry might not comply with DRY code principle, but I believe this would reduce user error, therefore this was inserted. 


After I imported the color package, the code was updated to:

```python

    # Function to remove truck from list
    def remove_truck(file_name):
        print(f"{header_function_colour}Remove truck from registry{reset}")
        # Display the current truck registry so that user knows what truck is in their list
        print(f"{header_function_colour}Current Truck Registry:{reset}")
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

        truck_rego_to_remove = input(f"{user_selection_color}Enter truck rego you want to remove: {reset}").upper()
        
        if truck_rego_to_remove.lower() == 'exit':
            print(f"{header_function_colour}Removing truck canceled. Returning to main page.{reset}")
            return

        truck_rego = []
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            # Flag to track if the truck to remove is found
            found = False  
            for row in reader:
                if truck_rego_to_remove == row[0]:
                    found = True
                else:
                    truck_rego.append(row)
            # Error handling if a truck rego that is not on the list has been entered
            if not found:
                print(f"{user_selection_color}Truck with registration number {truck_rego_to_remove} not found in the registry.{reset}")
    
        with open(file_name, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(truck_rego)


```
I added if condition of 'exit' so that the user can exit the function if they made an error and selected the wrong function to enter that area.

# Function - Truck weight classification
I original wanted this function to be where the user enters the rego of the truck that is already in the registry and it provides the weight classification. The weight classification is if the truck weights 12T or more it is heavy vehicle (HV), if it weights 8t or less then it is a light vehicle and everything else is medium class (MV). However, as a way to demonstrate that I am able to use the data input better, I have added the truck weight classification automatically so that it shows its class. The code I used to make it happen:

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

Since I have made changes to the original plan, I have decided to change the option 4 on the main page to a different function, where a user can search for trucks based on weight classification, and it only shows those trucks when requested. Please see below for the search based on weight classification function. 

# Function - Search based on weight classification / ordered view - removed
I tried to make a function that would only show trucks of ceratin weight class. I could not make this work. If I have time, I will come back to this and make this function. However, I thought the second best option is once the user enters the details of the truck and uses the function view truck registry, I would group them into classification automatically without the user requiring to take any action and make them feature into view truck regisrty. So to make this happened I changed the view truck function to include the following code:

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

However the following error code is coming up, please see below. If I can't fix it by end of 22/12 then I will remove this from the application and work on the other things I have planned. 

```console

    Traceback (most recent call last):
    File "/Users/gysohn/Desktop/Coder_Academy/T1A3/src/main.py", line 42, in <module>
        search_truck_classification(file_name)
    TypeError: search_truck_classification() missing 1 required positional argument: 'classification'

```
I coduln't get this to work in the time provided so it is not inlcuded in the final version. Will attempt to add in future version. 

# Function - Update truck details
I created a function in which a user could update the details of the truck in registry if it needed to be changed, as there could be user error in inputing the details. I wanted a different solution then removing the truck and re-adding the truck again. To do this I used the following code:

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
After I imported the color package, the code was updated to:

```python
    # Function to allow truck details to be udpated in the register
    def update_truck_details(file_name):
        print(f"{header_function_colour}Update truck details in the registry{reset}")
        # Display the current truck registry so that the user knows what trucks are in their list
        view_truck_registry(file_name)

        truck_rego_to_update = input(f"{user_selection_color}Enter truck rego you want to update: {reset}").upper()
        truck_registry = []

        with open(file_name, "r") as f:
            reader = csv.reader(f)
            # flag to track if the truck to update is found
            found = False
            for row in reader:
                if truck_rego_to_update == row[0]:
                    found = True
                    print(f"{option}Choose what to update:")
                    print("1. Registration Number")
                    print("2. Weight")
                    print("3. Both('reset')")
                    choice = input("Enter your choice (1, 2, or 3): ")
                    if choice == "1":
                        updated_rego = input("Enter the new registration number: ").upper()
                        # Keep the existing weight
                        updated_weight = row[1]  
                    elif choice == "2":
                        # Keep the existing registration number
                        updated_rego = row[0]  
                        updated_weight = get_valid_float_input ("Enter the new weight in tonnes (numbers only): ")
                    elif choice == "3":
                        updated_rego = input("Enter the new registration number: ").upper()
                        updated_weight = get_valid_float_input("Enter the new weight in tonnes (numbers only): ")
                    # Error handing for user input
                    else:
                        print(f"{invalid_error_color}Invalid choice. No updates will be made.{reset}")
                        return
                    updated_classification = classify_truck_weight(updated_weight)
                    truck_registry.append([updated_rego, 
                                        updated_weight, 
                                        updated_classification])
                else:
                    truck_registry.append(row)

        # Error handing if the wrong registration details are entered
        if not found:
            print(f"{invalid_error_color}Truck with registration number {truck_rego_to_update} not found in the registry.{reset}")
        else:
            with open(file_name, "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerows(truck_registry)
            print(f"{header_function_colour}Truck details updated successfully.{reset}")
```

After running a test on this function, I noticed that there was no eror handling for user input error, such as if the rego number is greater then 6 characters, if the rego is already on the list or the truck weight is not a float data. Therefore I updated the code to the below to include error checking:

```python

#Function to update truck details in the register
def update_truck_details(file_name):
    print(f"{header_function_colour}Update truck details in the registry{reset}")
    # Display the current truck registry so that the user knows what trucks are in their list
    view_truck_registry(file_name)

    truck_rego_to_update = input(f"{user_selection_color}Enter truck rego you want to update (or type 'exit' to go back to options): {reset}").upper()
    
    # Exit the update function and go back to options
    if truck_rego_to_update.lower() == 'exit':
        return

    truck_registry = []

    with open(file_name, "r") as f:
        reader = csv.reader(f)
        # flag to track if the truck to update is found
        found = False
        for row in reader:
            if truck_rego_to_update == row[0]:
                found = True
                print(f"{option}Choose what to update:")
                print("1. Registration Number")
                print("2. Weight")
                print("3. Both {reset}")
                choice = input("Enter your choice (1, 2, or 3), or type 'exit' to go back: ")
                # option for the user to exit the function
                if choice.lower() == 'exit':
                    print(f"{header_function_colour}Update canceled. Returning to the main page.{reset}")
                    return

                if choice == "1":
                    # User input for the new registration number with validation
                    while True:
                        updated_rego = input("Enter the new registration number: ").upper()
                        if len(updated_rego) <= 6 and not is_truck_registered(file_name, updated_rego):
                            break
                        else:
                            if len(updated_rego) >= 6:
                                print(f"{invalid_error_color}Invalid input. The truck registration can be 6 characters or less.{reset}")
                            else:
                                print(f"{invalid_error_color}Invalid input. The truck registration is already in the registry.{reset}")
                    # Keep the existing weight
                    updated_weight = float(row[1])
                elif choice == "2":
                    # Keep the existing registration number
                    updated_rego = row[0]
                    # User input for the new weight with validation
                    updated_weight = get_valid_float_input("Enter the new weight in tonnes (numbers only): ")
                elif choice == "3":
                    # User input for both registration number and weight with validation
                    while True:
                        updated_rego = input("Enter the new registration number: ").upper()
                        if len(updated_rego) <= 6 and not is_truck_registered(file_name, updated_rego):
                            break
                        else:
                            if len(updated_rego) >= 6:
                                print(f"{invalid_error_color}Invalid input. The truck registration can be 6 characters or less.{reset}")
                            else:
                                print(f"{invalid_error_color}Invalid input. The truck registration is already in the registry.{reset}")
                    updated_weight = get_valid_float_input("Enter the new weight in tonnes (numbers only): ")
                # Error handling for user input
                else:
                    print(f"{invalid_error_color}Invalid choice. No updates will be made.{reset}")
                    return

                updated_classification = classify_truck_weight(updated_weight)
                truck_registry.append([updated_rego, updated_weight, updated_classification])
            else:
                truck_registry.append(row)

    # Error handling if the wrong registration details are entered
    if not found:
        print(f"{invalid_error_color}Truck with registration number {truck_rego_to_update} not found in the registry.{reset}")
    else:
        with open(file_name, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(truck_registry)
        print(f"{header_function_colour}Truck details updated successfully.{reset}")


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
Further used error function if file could not be found based on what I learned during class. 

# Test of main functions

I designed two test to test the main functions, main page and update truck regisry. 

The two test can be found at:
Images/T1A3 - Test - Sheet1.pdf

# Python Packages
I have choosen to import the following packages:
- colored 
- numpy 
- pandas 
- requests 
- matplotlib
- os

To import the packages and functions, I wrote the following code:

```python
    from os import system
    from colored import fg, bg, attr
    import numpy as np
    import pandas as pd
    import requests
    import matplotlib.pyplot as plt
    from truck_registry_functions import (
        add_truck, 
        view_truck_registry, 
        remove_truck, 
        update_truck_details, 
        search_truck_classification)
```


Colored is the main function that I intend to use in my application. As the application developes I intend to use the others. 

For Colored, I used it in two different ways.

**Method 1**

I inserted the colour I wanted directly on the main.py file, as I wasn't going to use much different colours. Please see example below:

```python
    print(f"{fg('dark_khaki')}{bg('white')}Truck Register!{attr('reset')}")
```

**Method 2**

For the truck_registry_functions.py I required multiple colors and they needed to be repeated, so I created the function_colors.py page to define colors that I could use.

```python
    from colored import fg, bg, attr

    invalid_error_color = fg('red') + attr('bold')
    user_selection_color = fg('yellow')
    view_truck_registry_colour = fg('green')
    header_function_colour = fg('dark_khaki') + bg('white')
    option = fg('green')
    truck_rego_color = fg('blue')
    truck_weight_color = fg('light_green')
    truck_classification_color = fg('dark_violet_1a')
    reset = attr('reset')
```

Then I imported that to the truck_registry_functions.py 

```python

    from function_colors import (invalid_error_color, 
                                user_selection_color, 
                                header_function_colour, 
                                option, 
                                truck_rego_color, 
                                option, 
                                truck_rego_color,
                                truck_classification_color, 
                                truck_weight_color, reset)

```
Please see below of how I used it:

```python
   print(f"{header_function_colour}Add truck details to register{reset}")
```

I have also created a scrip file that would dowload all of the required packages and run the application, run.sh. It has the following code:

```bash
    #!/bin/bash

    # Ensure the correct language is installed
    check_python() {
        if command -v python3 &>/dev/null; then
            echo "Python 3 is installed."
        else
            echo "Error: Python 3 is not installed. Please install Python 3 to run this script."
            exit 1
        fi
    }

    #virtual enviroment download to ensure imports will work
    python3 -m venv .venv 
    source .venv/bin/activate
    pip3 install colored 
    pip3 install numpy 
    pip3 install pandas 
    pip3 install requests 
    pip3 install matplotlib
    python3 main.py

```

I also included a check for Python 3 as it is a requiremenet for the code to run. 

# Scrip files

In addition to the above scrip file I added two files:
- python3_check.sh - this file is present if the user wants to do an indepdent check on Python3 before they start the programme. This is optional as the run.sh checkes it as well. 
- internet_connection_check.sh - this files check if the user has connection to the internet. As internet is required to dowload the packages. I didn't add this to the run.sh file as there are other ways to check and it is an option step in the instructional manual. 

# Reference List
    - van Rossum, G, Warsaw, B & Coghlan, N 2001, PEP 8 – Style Guide for Python Code | peps.python.org, viewed 15/12/23 <peps.python.org>
    -‌ GeeksforGeeks 2019, GeeksforGeeks | A computer science portal for geeks, viewed 15/12/23 <GeeksforGeeks.>‌
    W3Schools 2019, Python Tutorial, viewed 15/12/23 <W3schools.com>
    -‌ LAB, V n.d., colour: converts and manipulates various color representation (HSL, RVB, web, X11, ...), PyPI viewed 16/12/23 <c​https://pypi.org/project/colour/>
‌
