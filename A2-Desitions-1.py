# Decision Structures: Areas of Triangles
# Danitza Fuenzalida, CSD 110 - 9630, 4/27/2021

"""
Side note for all the number variables: They are stored as floats since more often than not
triangles in area calculations have decimal lengths and heights, so the user can input a
decimal number if they so desire.

"""


# Simple introductory paragraphs to tell the user what the program is for:
print("This is a program that tells you the area of two triangles, and which one is bigger!")
print("Please input all of the information accordingly:")

# This variable stores the base number of the first triangle:
baseTriangleOne = float(input("What's the base of the first triangle? "))

# This variable stores the height of the first triangle:
heightTriangleOne = float(input("What's the height of the first triangle? "))

# This is where the area of the triangle is calculated
# Area of a triangle: (height * base)/2
areaTriangleOne = (heightTriangleOne * baseTriangleOne) / 2

# This line prints the area of the first triangle. I'm not sure it's a requirement but it serves well for debugging.
print("The area of the first triangle is: " + str(areaTriangleOne))

# Ditto for these variables: This stores the base of the second triangle:
baseTriangleTwo = float(input("What's the base of the second triangle? "))

# This variable stores the height of the second triangle:
heightTriangleTwo = float(input("What's the height of the second triangle? "))

# This stores the area of the second triangle:
areaTriangleTwo = (heightTriangleTwo * baseTriangleTwo) / 2

# Again, this line prints the area of the second triangle. Mostly used for debugging.
print("The area of the second triangle is: " + str(areaTriangleTwo))

# If statement, very simple. If the area of the first triangle is bigger it prints it as such.
if areaTriangleOne > areaTriangleTwo:
    print("The first triangle has a bigger area!")

# If that's not the case, then it prints that the second triangle is bigger.
else:
    print("The second triangle has a bigger area!")
