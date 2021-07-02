# A3-1-Average Rainfall
# By: Danitza Fuenzalida
# This is a project that will calculate the amount of rainfall in a set number of years using nested loops.


# Simple welcome statement so that the user knows what to do
print("This is a program that will calculate the average rainfall over a period of years!")

# Variable that stores the number for how many years need to be calculated.
yearsNumber = int(input("How many years do you want to calculate "))

# If statement to validate input. Program will crash if user enters either a negative number or no number.
if yearsNumber <= 0 or yearsNumber == False:
    # Print statement warning user.
    print("Input a valid number!")
    # Exit function, it basically force resets the program.
    exit()
# This else statement is here so program doesn't get confused with an open if statement.
else:
    # Blank line so that program doesn't print anything unusual here.
    print("")


""" This variable is used to keep the outer loop - yearly - in check. If the variable is equal to yearsNumber
    then loop ends."""
yearsLoop = 0

""" This variable is used to keep the inner loop - monthly - in check. 
    If the variable is over 12, the loop will reset. """
monthLoop = 0

# This variable is used to help print the ending statement. A loop is used to make it work like a counter.
month = 1

# This variable tracks all the months that the program runs. That way it can be printed later.
allMonths = 0


# This variable is used similarly to help print the ending statement, using a counter every outside loop to help it go up.
year = 1


""" This variable is used as a holder. Turns out saving the user input as a sum over itself causes some very strange
    side effects, so I preferred to make a separate variable to save the sum that later get printed."""
monthlyRainfall = 0

#This is what prints the little stars in the ticket message.
print("********************")

# The outer loop. Condition is that it will end if the yearsLoop variable is bigger or equal to the years the user asked.
while yearsLoop < yearsNumber:

    # The inner loop. Condition is that monthLoop will reset if monthLoop hits 12.
    while monthLoop <= 12:

        # This is the input that gets printed to the console. Its formatted correctly, though oddly.
        userRainfall = float(input("Please input the number of rainfall for year " + str(year) + " month " + str(month) + " "))
        # This is what causes the input of the user (rainfall) to get saved to the variable that's going to be used to be printed later.
        monthlyRainfall += userRainfall
        # This is the variable to keep the counter that tracks the outside loop.
        monthLoop += 1
        # This counter is just used to help print the ending statement.
        month += 1

        # This adds a month to the variable every loop.
        allMonths += 1

        # This if statement is used to help loop the month loop.
        if monthLoop == 12:
            # This is used to make the counter for the outside loop go up.
            yearsLoop += 1
            # This resets the inner loop.
            monthLoop = 0
            # This resets the counter for the printed statements.
            month = 1
            # This also adds one more year to the printed statements.
            year += 1
        # While odd, this is what causes the text to actually print properly once the loop is over.
        if yearsLoop == yearsNumber:
            # Prints the star pattern in the ticket.
            print("***********************")

            # Prints the ending ticket. All variables are printed with str function.
            print("Number of months: " + str(allMonths) + " Total rainfall in inches: " + str(monthlyRainfall)
                  + " Average rainfall: " + str(monthlyRainfall / allMonths))

            # Exit function finishes the code once its done.
            exit()
