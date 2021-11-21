from random import randint

# Allows users to play a game with the computer
def NumberGuessing():
    low = int(input("Enter the lower number : "))
    high = int(input("Enter the upper number : "))
    computerGuess = randint(low, high)

    while low < high:
        counter = 0

        for i in range(5):
            userGuess = int(input(f"Number {low} and {high} : "))

            if userGuess == computerGuess:
                counter += 1
                return f"Correct! You used {counter} out of 5 guesses"

            elif userGuess > computerGuess:
                counter += 1
                print("Your guess is too high")

            elif userGuess < computerGuess:
                counter += 1
                print("Your guess is too low")

        if counter >= 5:
            return "You've used up all your tries. You lose"

    if low > high:
        print("Please make sure your low is greater than your high")
        NumberGuessing()

# Computer takes a random letter and user has to guess that letter
def LetterGuessing():
    pass

if __name__ == "__main__":
    print(NumberGuessing())