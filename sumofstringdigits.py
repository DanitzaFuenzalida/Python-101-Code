# Danitza Fuenzalida - Finals 1, 6/14/2021
# This program will sum a list of numbers that are given in a string.

def summarizer(userNumbers):

    userNumbers = input("Please, input a string of numbers: ")
    print(userNumbers)

summarizer()

"""
    # For loop to iterate over given string.
    for num in userNumbers:
        # If so that empty character is not counted, this prevents empty square from being the highest number.
        if char != " ":
            # If there is a character in the given dictionary, give the value a +1.
            if char in dictionary:
                dictionary[char] += 1
            # No empty space, if found, -1.
            # If its the first time finding that word, set it to 1.
            else:
                dictionary[char] = 1
    # print dictionary for testing purposes.
    print(dictionary)
    # Variable stores the most often found character.
    biggest = (max(dictionary, key=dictionary.get))

    # Return biggest variable
    return biggest


# main function, takes in a parameter called words.
def main():
    # Phrase variable, it takes it user input. This is the string that's going to be broken.
    phrase = input("Print your phrase here: ")
    # Variable to call the function char_finder, phrased is passed to it.
    x = char_finder(phrase)
    # Printing of the most repeated character.
    print("The most repeated character is: " + str(x))


main()
"""