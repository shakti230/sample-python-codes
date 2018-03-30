#Mary McDonagh, 2018-02-24
#Guessing Game
# https://stackoverflow.com/questions/20449427/how-can-i-read-inputs-as-integers

#Adapted from https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9

from random import randint

target = randint(1, 100)
guess = 101

print("Guess a number between 1 and 100")
while guess != target:
    guess = int(input("Please enter your guess: "))
    if guess == target:
        print("well done! you've guessed correctly!")
    elif guess < target:
        print("Too low!")
    else: 
        print("Too high!")

