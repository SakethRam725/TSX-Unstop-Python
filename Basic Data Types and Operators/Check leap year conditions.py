# This script checks whether a given year is a leap year.

# Get the year from the user
year = int(input("Enter a year: "))

# Check leap year conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# output
# Enter a year: 2013
# 2013 is not a leap year.