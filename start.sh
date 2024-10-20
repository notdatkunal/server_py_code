#!/bin/bash


python_interpreter="/usr/bin/python3"
virtualenv_name="venv"
source "$virtualenv_name/bin/activate"
# Specify the path to your Python file
python_file="main.py"  # Replace with the actual file name

# Run the Python file
$python_interpreter "$python_file"