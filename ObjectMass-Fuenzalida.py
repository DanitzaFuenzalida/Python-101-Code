#Object Mass Calculation.
# Danitza Fuenzalida.
""" Program will calculate the weight of an object in newtons, and then
    display a message on whether they are too light, heavy, or normal weight."""

# Variable that stores the mass of the object that was given by the user.
# Stored as a float so that it is compliant with scientific notation.
mass = float(input("What is the mass of your object?: "))

# Weight variable with calculation.
weight = mass * 9.8

# Print message so that user can know what the object's mass is in newtons.
# Not required but makes code run better and a little more information is given back to the user.
print("The object's weight is " + str(weight) + " newtons.")

# If statements: if the weight is over 100N, the print statement is that the object is heavy.
if weight > 100:
    # Said print statement.
    print("This is unusual, the object is much heavier than it should be!")
# Elif: if weight is under 10N, the print statement is that the object is light.
elif weight < 10:
    # Said print statement, ditto.
    print("This is unusual, the object is much lighter than it should be!")
# Else statement for objects that fall right between the range.
else:
    # Print statement saying that the weight is normal.
    print("The object's weight is normal")
