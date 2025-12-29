# Read a File and Handle Errors
# Problem Statement:  Write a Python program that:
# 1. Opens and reads a text file named sample.txt.
# 2. Prints its content line by line.
# 3. Handles errors gracefully if the file does not exist.

import os

filename = "sample.txt"
path = f"tutedude/assignment_4/{filename}"

if os.path.exists(path):
    with open(path, 'r') as file:
        print("Reading the file content:")
        for sl, line in enumerate(file, start=1):
            print(f"Line {sl}: {line.strip()}")
else:
    print(f"Error: The file '{filename}' was not found.")