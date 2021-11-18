import sorting
import searching

def Menu():
    print("########### Main Menu ###########")
    print("What would you like to do today?")
    # Moves to Sorting Algorithms
    print("1. Sort A Disordered Array")
    # Moves to Searching Algorithms
    print("2. Search Through An Array")
    # Moves to list of created programs
    print("3. Menu For All Programs Created")
    # Allows user to select choice
    choice = int(input("> "))

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    else:
        print("Not available")


if __name__ == "__main__":
    Menu()