import random

secret_number = random.randint(1, 5)
guess_count = 0

while True:
    guess = int(input("Guess the number: "))
    guess_count += 1

    if guess == secret_number:
        print("Congratulations, you guessed it!", guess, secret_number)
        break
    elif guess > secret_number:
        print("Oops, your guess is a bit high. Try again!")
    else:
        print("Nope, your guess is a bit low. Give it another shot!")

print(f"You made {guess_count} guesses.")