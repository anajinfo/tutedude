# Write and Append Data to a File
# Problem Statement: Write a Python program that:
# 1. Takes user input and writes it to a file named output.txt.
# 2. Appends additional data to the same file.
# 3. Reads and displays the final content of the file.

filename = "output.txt"
path = f"tutedude/assignment_4/{filename}"

text = input("Enter text to write to the file: ")
with open(filename, "w") as file:
    file.write(text + "\n")
print("Data successfully written to output.txt.")

append_text = input("\nEnter additional text to append: ")
with open(filename, "a") as file:
    file.write(append_text + "\n")
print("Data successfully appended.")

print("\nFinal content of output.txt:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())
