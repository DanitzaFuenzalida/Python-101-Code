# Assignment 1-IPO-3, by Danitza Fuenzalida

# Introductory statement so user knows that the program is for:
print("Hello, I am a program that calculates the volume of a trapezoidal prism. Please input the according "
      "measurements when prompted.")

""" The following variables store length, height, base width and top width
    respectively. All of them are also stored as floats in case user wants
    to input decimal units. 
"""
length = float(input("Enter the length of the prism: "))
height = float(input("Enter the height of the prism: "))
baseWidth = float(input("Enter the base width of the prism: "))
topWidth = float(input("Enter the top width of the prism: "))

# Calculation of volume using given formula
volume = length * height * ((baseWidth / topWidth) / 2)

""" This entire block is used to print the parameters on multiple lines.
    The parameters are also affected by the str function so that the 
    float numbers are turned into strings. Round function is used so that
    result isn't excessively long. 
"""
print("Prism: ")
print("Length: " + str(length))
print("Height: " + str(height))
print("Base Width " + str(baseWidth))
print("Top Width " + str(topWidth))
print("Volume: " + str(round(volume, 2)))


# The additional output of the reduced by 25% measurements.
print("Extra: Original Measurements reduced by 25%: ")

# Same original calculation, just multiplied by 0.25. Saved on to the original variable.
volume = 0.25 * (length * height * ((baseWidth / topWidth) / 2))

""" This entire block is identical to the previous one
    except that every variables is multiplied by 0.25. 
    That way we don't need to bother with a completely new
    set of variables. Round is again used so volume output isn't
    ludicrously big. 
"""
print("Prism Reduced by 25%: ")
print("Length: " + str(length *  0.25))
print("Height: " + str(height * 0.25))
print("Base Width " + str(baseWidth * 0.25))
print("Top Width " + str(topWidth * 0.25))
print("Volume: " + str(round((volume * 0.25), 2)))
