import math
import random
'''
Best practices for variables names in Python:
- Be succinct
- Underscore beween works (snake casing)
- variable name describes what it holds
'''

x = 7
y = 5

result = x + y
print(result)

#random decimal between 0 and 1
print(random.random())
#random integer between 1 and 10
print(random.randint(1, 10))
#random integer between 50 and 100
print(random.randint(50,100))
#random even integer between 2 and 100
print(random.randrange(2, 100, 2))