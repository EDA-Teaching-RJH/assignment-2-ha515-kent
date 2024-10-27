### Part Two -- your code goes here. 
import random

def main():

    random_num = random.randint(1,100)

    guess_num = int(input("Guess a number between 1 and 100. "))

    while guess_num != random_num:
        guess_num = int(input("Please guess again. "))

        if guess_num < random_num:
            print("Sadly that is incorrect. Your guess was too low. ")

        elif guess_num > random_num:
            print("Sadly that is incorrect. Your guess was too high. ")

    if guess_num == random_num:
        print("Well done! Your guess is correct.")

main()