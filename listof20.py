# Danitza Fuenzalida - 6/14/2021
# This program will show the highest, lowest, total and average numbers in a list of 20 given by the user.


# Main function.
def main():

    # Sum variable at zero now, will be used later to sum up all the numbers in the list.
    sum = 0

    # Counter variable to keep the index moving up in the for loop.
    counter = 0

    # UserNumber variable is the string of numbers given.
    userNumber = input("Give me a list of 20 numbers, separated by a space: ")
    # .split() to transform the string into a list.
    userNumberList = userNumber.split()

    # For loop that will count up in the userNumberList
    for x in userNumberList:
        # Variable that's used to keep the number in the index. This is later used to obtain the sum of the numbers.
        newNum = int(userNumberList[counter])
        # Variable thats the sum of the numbers
        sum += newNum
        # counter goes up.
        counter += 1
    # Length variable, is used to calculate the average of the numbers.
    length = len(userNumberList)
    # Average is sum / length of the list.
    average = sum / length


    # Print statement with min. Note: min and max act very erradically when numbers are extrememly high or low.
    print("The lowest number is: " + str(min(userNumberList)))
    # Print statement with max. Note: min and max act very erradically when numbers are extrememly high or low.
    print("The highest number is: " + str(max(userNumberList)))
    # Print statement with the sum variable
    print("The sum of the numbers is: " + str(sum))
    # Print statement with the average of the numbers.
    print("The average of the numbers is: " + str(average))

# Call of the main function.
main()