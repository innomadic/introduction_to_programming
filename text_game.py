'''
input
while 
random
'''
from random import randint 

#secret_number = 7
secret_number = randint(1, 10)
guess = int(input("Guess a number between one and ten.  "))

'''
if 7 == guess:
    print("Good job my friend")
else:
    print("Bad job")
    guess = int(input("Guess a number between   one and ten.  "))
'''
while secret_number != guess:
    print("Try again!")
    guess = int(input("Guess a number between one and ten.  "))

print("Good job my friend")

