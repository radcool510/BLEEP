#!/usr/bin/env bash

# Change directory to the location of the script
cd "$(dirname "$0")"

# Install the required packages from the requirements.txt file
pip install -r requirements.txt

# Create the condition file
touch condition

# Run the script as long as the condition file exists
while [ -e condition ]; do
    python3 main.py
    git pull origin main
done
