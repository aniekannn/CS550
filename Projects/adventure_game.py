'''
Name: Aniekan Ekanem
Date: September 20, 2023
Sources: Python While Loops: https://www.w3schools.com/python/python_while_loops.asp,
Reflection: I'm proud of my code, it took a lot of work but I'm excited. Recieved good feedback for enjoyment. Coding procces was difficult as times but still fun
Honor Code: On my honor I have neither given nor received unauthorized aid 
'''
# Choate student vs. Deerfield Student Game

# Intro
print("Welcome to the high school adventure game!")
print("This is an adventure game where your choices determine your destiny.")

# Scene sets at student applying to boarding schools
print('''Your first choice starts now! You applied to boarding schools and you got accepted into Deerfield and Choate! 
Choose which boarding school to attend.''')

# Deerfield vs. Choate choice
def chooseSchool():
    # Boarding School user input
    school_choice = input("Type in Deerfield or Choate to make your decision \n>>> ").lower()
   
    while True:
        # Run Choate Branch
        if school_choice == "choate":
            runChoate()
            break
        # Run Deerfield Branch
        elif school_choice == "deerfield":
            runDeerfield()
            break
        # If user input isn't either choice, give user opportunity to type in again
        elif school_choice != "deerfield" or school_choice != "choate":
            print("I don't understand. Please try again")
            chooseSchool()

# User chose Choate
def runChoate():
        #Choate Text
        print('''Nice Choice! You now attend Choate Rosemary Hall. Because you attend such an amazing and fun school, you feel at home 
instantly. Everyone adores you and you've solitified your friends. You are the new queen bee.
A new girl, Emma, that's been hanging out with you asks to be apart of your friend group. ''')
        # Runs new decision
        allowFriend()

def allowFriend():
     friend_choice = input("Will you let her join? (Yes/No) \n>>> ").lower()

     while True:
          # Yes, allow friend branch
          if friend_choice == "yes":
               acceptFriend()
               break
          # No, don't allow friend branch
          elif friend_choice == "no":
               rejectFriend()
               break
          # repeats question if user enters "weird" choice
          elif friend_choice != "yes" or friend_choice != "no":
            print("I don't understand. Please try again")
            allowFriend()

def acceptFriend():
        # More Text
        print('''Nice! Emma is now apart of your friend group! Because of this, you now have a rep for being really nice and friendly!
In fact, Emma suggests that you should run for student council. She says that you have a good shot at winning.''')
        # Run for Student Council (StuCo) function
        runForStuCo()

def rejectFriend():
        print('''Ok, Emma is not apart of your friend group. You have now made an opp (aka enenmy). You and Emma are now beefing.
You both are petty and have been scheming all week. You come up with a plan to "accidentally" spill your lunch on her.''')
        # Attack emma branch
        attackEmma()

def attackEmma():
    # User enters choice
    attack_choice = input("Will you attack Emma? \n>>> ").lower()

    while True:
        # Creates war if yes
        if attack_choice == "yes":
            war()
            break
        # girls are calm if no
        elif attack_choice == "no":
            peace()
            break

         # repeats question if user enters choice that could potentially break the code
        elif attack_choice!= "yes" or attack_choice != "no":
            print("I don't understand. Please try again")
            attackEmma()

# Function for War
def war():
    # Text: Final result
    print('''You went ahead with your plan and spilled the food on Emma. She screams at the top of her lungs and offically declares 
war on you. You and Emma suffer from strike after strike from eachother for the rest of your Choate career. The end!''')

#Function for peace 
def peace():
    # Text: Final result
    print(''' You decide not to go with the plan and you and Emma eventually become friends your sophmore year. You both become closer 
and you both become friends for life! The end!''')

def runForStuCo():
    # User enters input for stuCo choice
    run_choice = input("Will you run for Student Council? \n>>> ").lower()

    while True:
        # If yes run become pres function
        if run_choice == "yes":
            becomePresident()
            break
        # if no, run chill function
        elif run_choice == "no":
            chill()
            # make sure to break for all
            break
        # repeats question if user entry could potentially break the code
        elif run_choice != "yes" or run_choice != "no":
            print("I don't understand. Please try again")
            runForStuCo()

def becomePresident():
    # Text: Final result
    print("You ran for Student Council and won! You are now the form president and leader at Choate. Congrats! The end!")

def chill():
    # Text: Final result
    print('''You decided not to run for Student Council due to the amount of work and other responsiblities you have. It is a 
 respectable decision and your peers are understanding. Because you this you now become popular. The end!''')

#----------------------------------------------------------

# Deerfield Branch
def runDeerfield():
    # Deerfield Text with context
    # Will you sit with a girl for lunch?
    print('''Okay, Welcome to Deerfield Academy. Because you attend such a sad, sad, school, it's hard to adjust during your first
term of freshman year. You are a bit lonely and looking to make friends. You see a girl sitting alone during lunch.''')
    # Run first Deerfield Choice: Friends
    sitWithGirl()

def sitWithGirl():
    # User inputs choice with yes or no
    friend_choice = input("Will you sit down with her? (Yes/No) \n>>> ").lower()

    while True:
        # if yes, make friend function
        if friend_choice == "yes":
            makeFriend()
            break
        # if no, sit alone
        elif friend_choice == "no":
            sitAlone()
            break

        # repeats question if user entry could potentially break the code
        elif friend_choice != "yes" or friend_choice != "no":
            print("I don't understand. Please try again")
            sitWithGirl()

def makeFriend():
        # Text
        print("Nice, you are now sitting down with the girl at lunch. You guys chat but then she gets up to get some food. ")
        # Run get food choice
        getFood()

def getFood():
     # Get food with her choice
     lunch_choice = input("She asks you to walk up with her to get some food. Do you go? (Yes/No) \n>>> ").lower()

     while True:
        # if yes, run walk up function
        if lunch_choice == "yes":
            walkUp()
            # Make sure to break to prevent infinte loop
            break
        # if no, run sit down function
        elif lunch_choice == "no":
            sitDown()
            break
         # repeats question if user entry could potentially break the code
        elif lunch_choice != "yes" or lunch_choice != "no":
            print("I don't understand. Please try again")
            getFood()

def walkUp():
    # Text: Final result
    print('''You guys are now bonding and offically become friends. Being at such a sad, sad school, you now find some normalcy and 
feel better. The end!''')

def sitDown():
    # Text: Final result
    print('''You guys are not friends anymore and you feel more alone. You regret choosing Deerfield and for the rest of your life,
 wish you chose Choate. The end!''')
               

def sitAlone():
        # Text: Final result
        print('''Ok, you decided not to sit with her. You are still alone. You regret choosing Deerfield and for the rest of your life,
 wish you chose Choate. The end!''')

# Original function to start code
chooseSchool()


'''
Peer Feedback

Ria Tyagi: I really enjoyed playing this game and liked how interesting it is as a Choate student. The little Deerfield puns were enjoyable.
As feedback, however, it was difficult to read the next when it is all in a continuous paragraph. I would recommened writing each sentence 
by line so it's easier for the user to read and follow.

Sebastian Plunket: I had fun playing this game. I like the school rivalry concept and how reflective it is into their lives at school. 
For feedback, I would recommened creating a way to repeat the question or choice for the user if they enter something wrong. When I entered
a choice that wasn't either of the two options, the program broke, so I would recommened fixing that.

'''