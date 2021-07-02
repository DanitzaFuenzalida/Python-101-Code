# Vehicle Travel
# Danitza Fuenzalida.
# Program will calculate the distance of that a vehicle has traveled using a loop.

# Speed of the user's vehicle, in miles per hour.
speed = int(input("What is the speed of the vehicle in mph?: "))
# Hours that the vehicle has traveled.
time = int(input("How many hours has the vehicle traveled?: "))

# Distance variable that is used to calculate the distance the car has traveled.
distance = speed * time

# Holder variable that is used so that the distance is added on every loop.
# Will print same distance otherwise on every loop iteration.
totalDistance = 0
# Simple variable so that hours can count up on the print statement.
hourCounter = 0

# Loop has a range of 1 - it starts on hour 1 so that it doesn't print distance for hour 0 -.
# Has a reach of how many hours the user inputted + 1- otherwise it will stop before reaching the end of the time frame.
# It goes up by 1 every time so that hours are counted one by one.
for x in range(1, (time + 1), 1):
    # The calculated distance is added on every loop iteration so that it prints how long the vehicle has traveled total.
    totalDistance += distance
    hourCounter += 1
    # Print statement to the console, will print a statement for every hour (time) the loop has iterated.
    print("Distance traveled on hour " + str(hourCounter) + ": " + str(totalDistance) + " miles")

