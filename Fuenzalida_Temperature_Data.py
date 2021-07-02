# Danitza Fuenzalida, 05/24/2021, Assignment: A5 - List.
# Temperature program: Program requests the temperatures for the week from the user, then
# graphs said data with matplotlib, creating a line graph.


# Import matplotlib function.
import matplotlib.pyplot as plt


# Main function. All of the code is done here.
def main():
    # List of days of the week.
    day_List = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Creates the list of temperatures to be used later. List is empty, will later be filled with user data.
    tempList = []

    # Statement to let user know what the program does.
    print("Hello! This program will create a line graph based on the temperatures of the week! Please note"
          "that this is intended to work with Fahrenheit temperatures.")

    # Range loop that will stop after 7 days have passed.
    for x in range(1, 8, +1):
        # Enter temperature user input call, stored in a variable.
        # List of days is used to count days properly. X - 1 is used otherwise list starts on Tuesday.
        userTemp = input("Enter the temperature for day " + day_List[x - 1] + ": ")

        # Answers of the user getting appended
        tempList.append(float(userTemp))
        # X counter going up by 1 every time to count index number up.
        x += 1

    # Variable to store the average of the temperatures, which is the sum / length.
    # Rounded to two decimal numbers.
    average = round(sum(tempList) / len(tempList), 2)

    # Variable that stores the index for the coldest day of the week.
    coldestDay = tempList.index(min(tempList))
    # Variable that stores the index for the warmest day of the week.
    warmestDay = tempList.index(max(tempList))

    # Print of highest temperature value. Uses index variable to call proper day.
    print(day_List[coldestDay] + " was the coldest day with a temperature value of " + str(min(tempList)) + ".")
    # Print of lowest temperature value. Uses index variable to call proper day.
    print(day_List[warmestDay] + " was the warmest day with a temperature value of " + str(max(tempList)) + ".")
    # Print of average temperature with proper variable.
    print("Average temperature was: " + str(average))

    # This program displays a simple line graph.

    # Build the line graph with the lists we have.
    plt.plot(day_List, tempList)

    # Add the customizables:
    # Causes grid to be true (just makes it easier to read in my opinion)
    plt.grid(True)
    # Gives plot proper title.
    plt.title("Weekly Temperature Data")
    # Gives plot proper Y axis label.
    plt.ylabel("Temperature Values")
    # Gives plot proper X axis label.
    plt.xlabel("Days of the Week")

    # Display the line graph.

    # Turns on plot
    plt.show()

    return
# Call of main function.
main()
