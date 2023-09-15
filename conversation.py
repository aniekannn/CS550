'''
Name: Aniekan Ekanem
Date: September 11, 2023
Sources: Using python to Capitalize first letter: https://flexiple.com/python/python-capitalize-first-letter,
How to print in same line in Python: https://www.tutorialspoint.com/how-to-print-in-same-line-in-python
Reflection: I enjoyed this assignment; it felt like a puzzle
Honor Code: On my honor I have neither given nor received unauthorized aid 
'''

first_name = input("What is your name? \n>>> ")

print(f"Hi, nice to meet you! ", end="")

location = input(f"Hey, {first_name}, where are you from? \n>>> ").lower()

if location == "houston" or location == "nigeria":
    print("Oh no way? Me too! ", end="")
else:
    print(location.capitalize() + "! I've never been but I've heard such good things! ", end="")

specific_location = input("Where in " + location.capitalize() + " are you from? \n>>> ")
print("Oh nice! ", end="")

form_number = input(f"Hey {first_name}, what form are you in? \n>>> ")
if form_number == "3":
    print(f"Oh you're in {form_number}rd form ? That's cool! ", end="")
else:
    print(f"Oh you're in {form_number}th form? That's cool! ", end="")

dorm_name = input("What dorm are you in? \n>>> ").lower()

if dorm_name == "mem" or dorm_name == "memorial":
    print("Yes! It's the best dorm on campus!")
else:
    print(dorm_name.capitalize() + "! Hot take but Mem House is better" )


