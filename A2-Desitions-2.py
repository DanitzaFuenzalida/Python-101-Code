# Multi-way Structures: Shipping Charges
# Danitza Fuenzalida, 4/27/2021

# This is an introductory phrase so the user knows what the program is for.
print("Hello! I am a program that will calculate the shipping rate of a desired package!")

# This variable stores the package weight:
# Note, this is stored as a float for more accuracy in calculations.
packageWeight = float(input("What's the weight of your package? "))

# All of these statements break the weight calculation:
# Note: In all calculations, the round function is used to shorten answers to two digits.

# If the package is less or equal than 2 pounds, its multiplied by 1.10
if packageWeight <= 2:
    print("The shipping charge is " + str(round((packageWeight * 1.10), 2)))

# If the package is less or equal than 6 pounds, its multiplied by 2.20
elif packageWeight <= 6:
    print("The shipping charge is: " + str(round((packageWeight * 2.20), 2)))

# If the package is less or equal than 10 pounds, its multiplied by 3.70
elif packageWeight <= 10:
    print("The shipping charge is: " + str(round((packageWeight * 3.70), 2)))

# If the package is less or equal than 10 pounds, its multiplied by 3.80
elif packageWeight > 10:
    print("The shipping charge is: " + str(round((packageWeight * 3.80), 2)))

# This is just an error handler. It's unlikely to activate, but I added it just in case.
else:
    print("Error! Please try again!")
