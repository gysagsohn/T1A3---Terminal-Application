#!/bin/bash

# Check if there is an active internet connection
if ping -q -c 1 github.com &> /dev/null; then
    echo "Internet connection is active."
else
    echo "No internet connection. Please check your network settings."
fi