# A3-2 Sum of Numbers
# By: Danitza Fuenzalida
# This is a project that will calculate the sum of numbers that a user inputs.

# Introductory message to tell the user what the program does.
print("This is a program that will calculate the sum of numbers!")
# Further instructions, tells the user negative number will end program.
print("Please input a negative number at any point to exit the program.")

# Total variable that's going to be printed later
printSum = 0
# User inputted number. Should cancel if negative.
number = 0

# While loop. Meant to run until user submitted number is less than 0.
while number >= 0:
    # Number variable stores the positive numbers that the user submits.
    number = int(input("Enter a positive number: "))
    # printSum saves the user numbers to be shown later in the print statement.
    printSum += number
""" When program ends, it will subtract the last number from list 
    - which, due to always being negative, it will always be 0. """
printSum -= number
# Ending print statement.
print("The sum of positive numbers is: " + str(printSum))
