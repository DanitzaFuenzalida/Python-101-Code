# Danitza Fuenzalida, 06/03/2021, Assignment: A6 - Dictionary.
# Temperature program: Print list of temperatures given by a user.

# Main function. All of the code is done here.
def main():
    # Dictionary with days of the week.
    weeklyTemps = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0,
                   "Friday": 0, "Saturday": 0, "Sunday": 0}

    # Statement to let user know what the program does.
    print("Hello! This is a program that will ask you for the temperatures of the week.")
    # Variable that will be compared to later. Absurdly huge number on purpose.
    coldestTemp = 100000000000
    # Coldest day variable, placeholder for coldest day.
    coldestDay = " "

    # Variable that will be compared to later. Absurdly low number on purpose.
    warmestTemp = -100000000000
    # Warmest day variable, placeholder for warmest day.
    warmestDay = " "

    # Range loop that will stop after end of the dictionary.
    for key in list(weeklyTemps):
        # User temp variable. Value is called for each dictionary key, counting up with x.
        userTemp = int(input("Enter the temperature for " + str(key) + ": "))
        # New values are pushed into the dictionary.
        weeklyTemps[key] = userTemp

        # If statement on loop, constantly checks if user temperature is above WarmestTemp variable.
        if userTemp > warmestTemp:
            # If true, warmestTemp is now user temperature.
            warmestTemp = userTemp
            # Retrieve the key associated with the warmest temperature.
            # Works because key variable acts as a counter in loop.
            warmestDay = key

        # If statement on loop, constantly checks if user temperature is below coldestTemp variable.
        if userTemp < coldestTemp:
            # If true, coldestTemp is now user temperature.
            coldestTemp = userTemp
            # Retrieve the key associated with the coldest temperature.
            # Works because key variable acts as a counter in loop.
            coldestDay = key

    # Coldest day print, with coldestDay and Temp variables as placeholders.
    print(str(coldestDay) + " was the coldest day with a temperature value of " + str(coldestTemp) + ".")

    # Warmest day print, with coldestDay and Temp variables as placeholders.
    print(str(warmestDay) + " was the coldest day with a temperature value of " + str(warmestTemp) + ".")

    # Variable to store the average of the temperatures, which is the sum of all the values, divided by 7.
    average = int(sum(weeklyTemps.values()) / 7)
    # Round the average
    average = round(average)
    # Print the average
    print("The average temperature was " + str(average))

    # List that's going to be used to be printed later, above average temperature days.
    aboveList = []

    # Loop to find above average temperature days. Works same way as other for loop.
    for key in list(weeklyTemps):
        # Creates a new variable UserTemp, inserting user's key.
        userTemp = weeklyTemps[key]
        # If the user value is above average.
        if userTemp > average:
            # It adds the key to the list of days.
            aboveList.append(key)

    # Variable to format list better for printing.
    abovePrint = ', '.join(aboveList)
    # Print days above average.
    print("Days where temperature was above average: " + abovePrint)


# Call of main function.
main()
