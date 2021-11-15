# Allows user to select a searching mechanism
def Menu(Array):
    print("Searching Mechanisms Available\n"
          "1. Linear Search\n"
          "2. Binary Search\n\n"
          "Select an option with the number in front of it")

    choice = int(input("> "))

    if choice == 1:
        LinearSearch(Array)
    elif choice == 2:
        print("Coming Soon...")
    else:
        print("Choice not available")
        Return(Array)

# When a user wants to go back to the Menu
def Return(Array):
    request = input("Return to Menu?(y/n)")

    if request.Upper() == "Y":
        Menu(Array)
    elif request.Upper() == "N":
        print("Good bye!")

# Main area for running functions and/or procedures in order
if __name__ == "__main__":
    userArray = []
    arrayLen = int(input(f"Number of elements in array : "))
    Counter = arrayLen

    # Allows user to fill array with data
    for index in range(arrayLen):
        num = int(input("Num : "))
        Counter = Counter - 1

        if Counter > 1:
            print(f"{Counter} numbers left...")
        elif Counter == 1:
            print(f"{Counter} number left...")

        userArray.append(num)

    # Initializes the menu
    Menu(userArray)