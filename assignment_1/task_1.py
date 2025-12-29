# Perform Basic Mathematical Operations
# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
	# o	Addition
	# o	Subtraction
	# o	Multiplication
	# o	Division
# 3.  Displays the results of each operation on the screen.

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print(
    "\nAddition: ", int(first_number) + int(second_number),
    "\nSubtraction: ", int(first_number) - int(second_number),
    "\nMultiplication: ", int(first_number) * int(second_number),
    "\nDivision: ", int(first_number) / int(second_number)
    )