# Danitza Fuenzalida - A7: Most Frequent Character 6/9/2021
# This program will convert a string to pig latin.

# Define the main function.
def main():
    # Empty list that's going to be used to track the new pig latin words.
    pigList = []

    # User will input a phrase, its stored in phrase.
    phrase = input("Enter a phrase to translate to pig latin: ")

    # Divides the phrase given into a list.
    phraseList = phrase.split()

    # ay is a variable so that if word is uppercase, .upper() can be used.
    ay = "ay"

    # For loop, will iterate for every word in the list.
    for word in phraseList:
        # Takes first letter of the phrase, sliced as index 1.
        # Counter variable is also used to keep track of the item position in the list.
        firstLetter = (word[slice(1)])

        # Phrase is updated so that the first letter is no longer in it.
        # Again, using counter to track the list position.
        slicedPhrase = word[1:]

        # This checks to see if the first letter of the word is in uppercase.
        # If it is, the "ay" will also be uppercase.
        if firstLetter.isupper():
            # pigLatin variable is the sliced phrase, plus first letter plus uppercase "ay".
            pigLatin = slicedPhrase + firstLetter + ay.upper()
            # Append variable to the pigLatin list.
            pigList.append(pigLatin)

        else:
            # pigLatin variable is the sliced phrase, plus first letter plus "ay".
            pigLatin = slicedPhrase + firstLetter + ay
            # This is appended to the pigLatin list.
            pigList.append(pigLatin)
            # After all that, counter moves up, letting it take care of the next word.

    # Printing of the list using the join function.
    print(' '.join(pigList))


# Call of the main function.
main()
