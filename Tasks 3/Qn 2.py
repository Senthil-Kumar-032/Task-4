# Word Scramble Game

words = ['Python', 'Javascript', 'Java', 'Automation', 'Pytest', 'Guvi', 'Selenium']

# To select the value from the list
word = words[0]

# Scrambled the word using String Manipulation
scrambled = word[::-1]

print("Scrambled word:", scrambled)

guess = ""

# Loop to check the word until correct
while guess != word:
    guess = input("Enter your guess: ")

    # Check if the guessed word is correct
    if guess == word:
        print("Correct guess")
    else:
        print("Wrong guess, try again")
