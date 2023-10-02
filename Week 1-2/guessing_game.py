import random

'''
Name: Aniekan Ekanem
Date: September 14, 2023
Sources: Python While Loops: https://www.w3schools.com/python/python_while_loops.asp,
Reflection: I enjoyed this assignment; it was fun
Honor Code: On my honor I have neither given nor received unauthorized aid 
'''

#Intro statement
print("Welcome to my guessing game! The number is between 1 and 200!")
#Print random int between 1 and 200
random_int = random.randint(1, 200)
#User insert guess
guess = int(input("Enter your guess \n>>> "))

#Conditions if random int isn't guessed
while random_int != guess:
    #Condition if guess is too small 
    if guess < random_int:
        print("Too low, try again! ")
        #opportunity to guess again
        guess = int(input("Enter your guess again \n>>> "))
    elif guess > random_int:
        #Condition if guess is too big 
        print("Too high, try again! ")
        #opportunity to guess again
        guess = int(input("Enter your guess again \n>>> "))
    #Make sure to break to avoid infinite loop
    else:
        break
#Print end message
print("Congrats!!! You guesses the number!")
