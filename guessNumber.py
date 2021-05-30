import random

name = "Dorian"

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while(guess != random_number):
        guess = int(input("Guess a number a between 1 and {x} "))
        if guess < random_number:
            print("Sorry, guess again.Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high")

    print(f"Congrats. You have guessed the number {random_number}")


def computer_guess(x):
    low = 1
    high = x
    feeback = ''

    while feeback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        feeback = input(
            f"Is {guess} too high (H), too low (L), or correct (C)?").lower
        if feeback == 'h':
            high = guess - 1
        elif feeback == 'l':
            low = guess + 1
    print(f"The computer guees you number, {guess}, correclty")

