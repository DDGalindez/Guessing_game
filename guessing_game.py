import random

def guessing_game():

    secret_number = random.randint(1, 10)
    attempts = 0

    print("Guess a number from 1-100")

    while True:

        guess = int(input("Your guess: "))
        attempts += 1

    
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Try again. The correct number is higher.")
        else:
            print("Try again. The correct number is lower.")


guessing_game()