from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
your_choose=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

comp_number=random.randint(0, 100)

def play(attempts):
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess < comp_number:
            print("Too low!")
            print("Guess again.")
        elif guess > comp_number:
            print("Too high!")
            print("Guess again.")
        else:
            print(f"You got it! The answer was {comp_number}.")
            return
        attempts -= 1
    print("You've run out of guesses. You lose.")
    print(f"The number was {comp_number}.")

if your_choose == "easy":
    play(10)
elif your_choose == "hard":
    play(5)
else:
    print("Invalid choice. Please type 'easy' or 'hard'.")