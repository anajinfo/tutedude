# Calculate Factorial Using a Function
# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.

number = int(input("Enter a number: "))

def factorial(n):
	if n < 0:
		return "Factorial is not defined for negative numbers"
	elif n == 0 or n == 1:
		return 1
	else:
		result = 1
		for i in range(2, n + 1):
			result *= i
		return result

result = factorial(number)
print(f"Factorial of {number} is: {result}")
