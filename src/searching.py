# Scans through all elements for a wanted number
def LinearSearch(Array):
    print(Array)
    itemWanted = int(input("Please select a number you want : "))
    itemFound = False
    itemIndex = 0

    for ind in range(len(Array)):
        if itemWanted == Array[ind]:
            itemFound = True
            itemIndex = ind
            break
        else:
            itemFound = False

    if itemFound:
        print(f"Item found at index : {itemIndex}")
    else:
        print("Item not in store")

# Scans through circularly sorted arrays
def circularArraySearch(CircularArray):
    lowerBound = 0
    upperBound = len(CircularArray)
    itemWanted = int(input("Enter Number : "))

    while lowerBound < upperBound:
        midpoint = lowerBound + round((upperBound - low) / 2)

        if CircularArray[midpoint] == itemWanted:
            print(f"Item found at index {midpoint}")
            break

        if CircularArray[lowerBound] <= CircularArray[midpoint]:
            if itemWanted >= CircularArray[lowerBound]:
                # This needs to be worked on immediately
                pass

# Scans through elements by mid for wanted number
def BinarySearch(Array):
    upperBound = len(Array)
    lowerBound = 0
    count = 0
    itemWanted = int(input("Enter Number : "))

    while count < len(Array) - 1:

        midpoint = round(lowerBound + ((upperBound - lowerBound) / 2))

        if lowerBound > upperBound:
            print("Item not in store")
            break

        else:
            if Array[midpoint] == itemWanted:
                print(f"Item found at index {midpoint}")
                break

            elif Array[midpoint] > itemWanted:
                upperBound = midpoint - 1

            elif Array[midpoint] < itemWanted:
                lowerBound = midpoint + 1

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
        BinarySearch(Array)
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