# Required imports
from random import randint

# Allows users to play a game with the computer
def NumberGuessing():
    # User can now select difficulty
    print("Please select a mode"
          "1. Easy"
          "2. Hard")
    choice = int(input("> "))
    low = int(input("Enter the lower number : "))
    high = int(input("Enter the upper number : "))
    computerGuess = randint(low, high)

    while low < high:
        counter = 0

        for i in range(5):
            userGuess = int(input(f"Number {low} and {high} : "))

            if userGuess == computerGuess:
                counter += 1
                return f"Correct! {counter} out of 5 guesses used"

            elif userGuess > computerGuess:
                counter += 1
                print("Your guess is too high")

            elif userGuess < computerGuess:
                counter += 1
                print("Your guess is too low")

        if counter >= 5:
            return "All tried used. You lose!"

    if low > high:
        print("Upper must be greater than Lower")
        NumberGuessing()

# Computer takes a random letter and user has to guess that letter
def LetterGuessing():
    Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
               "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
               "U", "V", "W", "X", "Y", "Z"]
    selectedIndex = randint(0, 25)
    computerGuess = Letters[selectedIndex]
    counter = 0

    for i in range(5):
        userGuess = str(input("Input A Letter : "))

        if userGuess.upper() == computerGuess.upper():
            counter += 1
            return f"Correct! {counter} out of 5 guesses used"

        else:
            counter += 1
            print("Incorrect!")

    if counter >= 5:
        return f"Answer was {computerGuess}. You lost!"

# Takes care of all the games for user to select
def GamesMenu():
    pass

if __name__ == "__main__":
    print(LetterGuessing())