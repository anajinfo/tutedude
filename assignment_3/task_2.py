# Using the Math Module for Calculations
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
	# o   Square root of the number
	# o   Natural logarithm (log base e) of the number
	# o   Sine of the number (in radians)
# 3.   Displays the calculated results.


number = int(input("Enter a number: "))

import math

sqrt_result = math.sqrt(number)
log_result = math.log(number)
sine_result = math.sin(number)

print(f"Square root: {sqrt_result}")
print(f"Logarithm: {log_result}")
print(f"Sine: {sine_result}")
