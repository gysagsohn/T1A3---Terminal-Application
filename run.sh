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

