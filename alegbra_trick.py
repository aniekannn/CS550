import math

print(f"Welcome to my magic number machine! To start,", end="")
og_number = int(input(" enter a random  number \n>>> "))

new_number = og_number + 40
new_number *= 4
new_number -= 169
special_value = new_number/4

input("Add 40 to your number \n>>> ")
input("Next, multiply your number by 4 \n>>> ")
input("After, subtract the product by 160 \n>>> ")
input("Finally, divide that number by 4 \n>>>")
print(f"Was your number {special_value}?")


