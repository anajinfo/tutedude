# Sum of Integers from 1 to 50 Using a Loop
# Problem Statement: Write a Python program that:
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.

total_sum = 0

for number in range(1, 51):
    total_sum += number

print("The sum of integers from 1 to 50 is:", total_sum)
