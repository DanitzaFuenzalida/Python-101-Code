#Tip, Tax, Total.
# Danitza Fuenzalida.
# Program will calculate the tax and tip off of the meal check, and then will sum it to the total.

# Variable check is how much the food cost for the user.
# Formatted with floats since usually checks are not rounded.
check = float(input("How much is your food total?: "))

# Calculating the check out of a 15% off of the original value.
tip = check * 0.15

# Calculating the tax out of 7% off of the original check value.
tax = check * 0.7

# Total is the original check, plus the tax and tip values.
total = check + tax + tip

# Final print statement, with dollar sign and correct use of format function.
print("The total plus tax and tip is: " + "$" + format(total, '.2f'))
