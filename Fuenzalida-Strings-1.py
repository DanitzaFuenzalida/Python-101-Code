# Danitza Fuenzalida - A7: Most Frequent Character 6/9/2021
# This program will calculate which is the most frequent character in a string that the user gives it.

def char_finder(phrase):
    # Empty dictionary.
    dictionary = {}

    # For loop to iterate over given string.
    for char in phrase:
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