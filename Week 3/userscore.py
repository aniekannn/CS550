user_score = 0
def level1():
    global user_score
    user_score +=3

def level2():
    global user_score
    user_score -= 1

def level3():
    global user_score
    user_score += 4
    
'''
scope:
- where a variable can be recognized in the code
- if you have a variable defined within a funciton, then you 
can't use it outside the funciton because it is a local variable to the function
'''

level3(level2(level1()))

level1()
level2()
level3()

print(user_score())