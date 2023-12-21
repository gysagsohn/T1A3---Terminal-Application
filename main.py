#T1A3 terminal application - crearting repository

from colored import fg, bg, attr
from os import system
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
from truck_registry_functions import add_truck, view_truck_registry, remove_truck, update_truck_details, search_truck_classification

file_name= "registry.csv"

try:
    truck_registry_file= open(file_name, "r")
    truck_registry_file.close()
except FileNotFoundError:
    truck_registry_file = open(file_name, "w")
    truck_registry_file.write("rego,weight,classification\n")
    truck_registry_file.close()


print(f"{fg('dark_khaki')}{bg('white')}Truck Register!{attr('reset')}")


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

users_choice = ""

while users_choice != "6":
    users_choice = truck_registry()
    if (users_choice == "1"):
        add_truck(file_name)
    elif (users_choice == "2"):
        view_truck_registry(file_name)
    elif (users_choice == "3"):
        remove_truck(file_name)
    # elif (users_choice == "4"):
    #     weight_classification_truck(file_name)
    elif (users_choice == "5"):
        search_truck_classification(file_name)
    elif (users_choice == "6"):
        continue
    else:
       print(f"{fg('red')}{attr('bold')}Invalid Input{attr('reset')}")


print(f"{fg('yellow')}{bg('cyan')}Goodbye! Thank you for using the truck registry{attr('reset')}")