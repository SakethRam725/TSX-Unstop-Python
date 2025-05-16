# This script compares two numbers entered by the user.

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the numbers and print the result
if num1 > num2:
    print("The first number is greater than the second number.")
elif num1 < num2:
    print("The first number is less than the second number.")
else:
    print("The first number is equal to the second number.")

# output example
# Enter the first number: 23
# Enter the second number: 12
# The first number is greater than the second number.