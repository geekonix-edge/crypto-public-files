import random

def guess_number():
    secret_number = random.randint(1, 100)
    while True:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess == secret_number:
            print("Congratulations! You guessed the correct number and your OTP is amitkumar")
            break
        elif guess < secret_number:
            print("The number is greater than your guess. Try again!")
        else:
            print("The number is smaller than your guess. Try again!")
guess_number()
