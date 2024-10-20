#!/bin/bash

if [[ "$OSTYPE" == "msys" ]]; then
    python_interpreter="python"
else
    python_interpreter="/usr/bin/python3"
fi
# Specify the path to your Python file
python_file="main.py"  # Replace with the actual file name

# Run the Python file
$python_interpreter "$python_file"