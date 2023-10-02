'''
lists
store multiple values together
one "variable" (the list) that contains all the values you need
group data that's related
'''

import random

alist = [] # empty list
blist = [5, 2, 5, 4]

print(blist)
print(*blist)# prints without notation

# to duplicate line shift+command+d

empty = []
empty.append("apple")
empty.append("banana")

print(empty)
empty.insert(2, "strawberry")
print(empty)

#del empty[2]
#empty.remove("strawberry")

removed_item = empty.pop(2)#gives value taken out of list
print(empty, removed_item)

#Problem 1
ran_list = []

for x in range(100):
    num_one = random.randint(1,30)
    ran_list.append(num_one)

print(*ran_list)

#Problem 2
div_list = []
num1 = 0

for x in range(11):
    num1 += 7
    div_list.append(num1)

print(*div_list)

#Problem 3

prob3_list = []

while len(prob3_list) < 25:
    prob3_list.append(random.randint(2,100) * 2)

print(*prob3_list)
    


