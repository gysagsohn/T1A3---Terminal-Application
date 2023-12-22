#!/bin/bash

python3 -m venv .venv #virtual enviroment download to ensure imports will work
source .venv/bin/activate
pip3 install colored 
pip3 install numpy 
pip3 install pandas 
pip3 install requests 
pip3 install matplotlib
python3 main.py




