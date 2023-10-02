import random

'''
Name: Aniekan Ekanem
Date: September 19, 2023
Sources: Python While Loops: https://www.w3schools.com/python/python_while_loops.asp,
How do i repeat the game on a loop?: https://stackoverflow.com/questions/39933029/how-do-i-repeat-the-game-on-a-loop
Reflection: Tough challenge, but fun, if the user enters anything other than an integer,the program breaks
Honor Code: On my honor I have neither given nor received unauthorized aid 
'''

def game():
    #Intro statement
    print("Welcome to my guessing game! The number is between 1 and 200!")
    #Print random int between 1 and 200
    random_int = random.randint(1, 200)
    #User insert guess
    guess = input("Enter your guess \n>>> ")

    #Conditions if random int isn't guessed
    while play_again == "y":
        #Condition if guess is too small 
        if guess < random_int:
            print("Too low, try again! ")
            #opportunity to guess again
            guess = input("Enter your guess again \n>>> ")
        elif guess > random_int:
            #Condition if guess is too big 
            print("Too high, try again! ")
            #opportunity to guess again
            guess = input("Enter your guess again \n>>> ")
        else:
            print("I don't understand, please type an integer betweem 1 and 200")
print("Congrats!!! You guesses the number!")

#conditions while true
while True:
    #ask user to play again
    play_again = str(input("Want to play again? y/n \n>>> "))
    #if yes run function
    if play_again == "y" or play_again == "yes":
        game()
    #if no break
    elif play_again == "no" or play_again == "n":
        print("Okay, thank's for playing!")
        break
    # Condition if not read
    else:
        print("I don't understand, please type again in lowercase with either y or n")
