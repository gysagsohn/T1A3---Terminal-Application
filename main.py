#T1A3 terminal application - crearting repository

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
    )


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
    print(f"{fg('green')}1. Enter 1 add truck rego and weight to your list {attr('reset')}")
    print(f"{fg('green')}2. Enter 2 to view your truck registry {attr('reset')}")
    print(f"{fg('green')}3. Enter 3 remove truck from your registry {attr('reset')}")
    print(f"{fg('green')}4. Enter 4 to update truck details in registry {attr('reset')}")
    print(f"{fg('green')}5. Enter 5 to exit {attr('reset')}")
    choice = input(f"{fg('yellow')}Enter your selection: {attr('reset')}")
    return choice


users_choice = ""


while users_choice != "5":
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
        continue
    else:
       print(f"{fg('red')}{attr('bold')}Invalid Input{attr('reset')}")


print(f"{fg('yellow')}{bg('cyan')}Goodbye! Thank you for using the truck registry{attr('reset')}")