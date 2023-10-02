'''
Name: Aniekan Ekanem
Date: September 11, 2023
Sources: Using python to Capitalize first letter: https://flexiple.com/python/python-capitalize-first-letter,
How to print in same line in Python: https://www.tutorialspoint.com/how-to-print-in-same-line-in-python
Reflection: I enjoyed this assignment; it felt like a puzzle
Honor Code: On my honor I have neither given nor received unauthorized aid 
'''
#Ask user for name
first_name = input("What is your name? \n>>> ")

#As response, print greeting
print(f"Hi, nice to meet you! ", end="")

#Use name variable to ask 2nd Question
location = input(f"Hey, {first_name}, where are you from? \n>>> ").lower()#Use lower function to case correct user input

#Set if statement for different responses for 2nd question
if location == "houston" or location == "nigeria":
    #Agreement response
    print("Oh no way? Me too! ", end="")
else:
    #Inquiry response
    print(location.capitalize() + "! I've never been but I've heard such good things! ", end="")#Capitalizes user response to location question

#3rd Question
specific_location = input("Where in " + location.capitalize() + " are you from? \n>>> ")#Capitalizes user response to location question
#Response
print("Oh nice! ", end="")

#4th Question, uses name variable
form_number = input(f"Hey {first_name}, what form are you in? \n>>> ")

#Set if statement for different ending of number th, rd, st
if form_number == "3":
    print(f"Oh you're in {form_number}rd form ? That's cool! ", end="")
else:
    print(f"Oh you're in {form_number}th form? That's cool! ", end="")

#5th Question and lowercases response
dorm_name = input("What dorm are you in? \n>>> ").lower()

#Agreement if statement
if dorm_name == "mem" or dorm_name == "memorial":
    #Agreement response
    print("Yes! It's the best dorm on campus!")
else:
    #Clapback response
    print(dorm_name.capitalize() + "! Hot take but Mem House is better" )


