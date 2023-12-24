
#!/bin/bash

# Check if Python 3 is installed
if command -v python3 &> /dev/null; then
    echo "Python 3 is installed."
else
    echo "Python 3 is not installed. Please install it before running this script."
fi