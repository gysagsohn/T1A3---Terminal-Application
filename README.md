Started my project of T1A3 Terminal application
My app idea was approved and this was the brief I submitted:
    Brief - I would like to make a truck register. It will keep a detail for a fleet of trucks, including key information, such as rego, model, and plant number.

    Features will include:
        to add/remove trucks
        to update the data relevant to the truck
        ability to search/sort data by any of its features
        display the register of trucks
        a feature that defines a truck based on its GVM to be LV, MV, HV

Remote Repository
    For my remote repository I have choosen git hub. The first commite was made on 12/12


Project managment tool
    Trello - planning to use trello to manage the process and will be added to this project submission
    Screen shot of the board on day 1 can be found at T1A3/docs/trello_board_day1

CODE STYLE CONVENTIONS:
    Pep 8 has been choosen as the style convention.


Main page - function 1 part 1 and user input 1w
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

Users Choice - fuction 1 part 2

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

CSV file 

Need a CSV file to hold the truck register informaiton. Created "registery.csv" function to record the list 

    ```python
    file_name= "registery.csv"

    try:
        truck_registery_file= open(registery.csv, "r")
        truck_registery_file.close()
        print("In try block")
    except FileNotFoundError:
        truck_registery_file = open(file_name, "w")
        truck_registery_file.write("title,completed\n")
        truck_registery_file.close()
        print("In except block")
    ```
Further used error function to check. Based on what I learned during class. As of 18/12 this has not been tested, and might be updated as it develops. 