# Assignment 1-IPO-2, by Danitza Fuenzalida

# This is just an introductory message so the user knows what to do
print("Hello, I am a temperature converter. I convert from Fahrenheit to Kelvin")

""" This is where the Fahrenheit variable is stored. 
    Made it a float number in case people want to use
    decimal temperatures. You never know.  
"""
f = float(input("Input Fahrenheit temperature to convert: "))

# This is where the calculations happen, using the farenheit formula.
k = (f + 459.67) * (5/9)

""" Here's the final message. Used the round function so that answer
    isn't absurdly long, rounded to two decimals.  
"""
print("The new temperature is: " + str(round(k , 2)) + " Kelvin")