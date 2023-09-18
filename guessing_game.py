import random

'''
Name: Aniekan Ekanem
Date: September 14, 2023
Sources: Python While Loops: https://www.w3schools.com/python/python_while_loops.asp,
Reflection: I enjoyed this assignment; it was fun
Honor Code: On my honor I have neither given nor received unauthorized aid 
'''

#Intro
print("Welcome to my guessing game! The number is between 1 and 200!")
#Print random int between 1 and 200
random_int = random.randint(1, 200)
#User insert guess
guess = int(input("Enter your guess \n>>> "))

while random_int != guess:
    if guess < random_int:
        print("Too low, try again! ")
        guess = int(input("Enter your guess again \n>>> "))
    elif guess > random_int:
        print("Too high, try again! ")
        guess = int(input("Enter your guess again \n>>> "))
    else:
        break
print("Congrats!!! You guesses the number!")
