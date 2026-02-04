# Guess the Number Game

# number to be guessed
number = 3

print("Guess a number between 1 and 10")

# Program runs until correct guess
while True:
    guess = int(input("Enter your guess: "))

    # checks the number is too high or too low or correct
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    # If the number is correct it will break the loop
    else:
        print("Correct Number Found")
        break

