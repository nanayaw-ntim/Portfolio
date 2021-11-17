# Sorts array given using relatively unreliable speed
def BubbleSort(Array):
	sortingArray = Array
	sortedArray = []

	# Loops through array to sort elements
	for i in range(len(sortingArray)):
		currentValue = 0
		for ind in range(len(sortingArray) - 1):
			if sortingArray[ind] > sortingArray[ind + 1]:
				currentValue = sortingArray[ind]
				sortingArray[ind] = sortingArray[ind + 1]
				sortingArray[ind + 1] = currentValue

	print(f"Your sorted array is : {sortingArray}")

# Sort array with O(logN) sorting method
def InsertionSort(Array):
	pass

# Allows user to select a sorting mechanism
def Menu(Array):
	print("Sorting Mechanisms Available\n"
		  "1. Bubble Sort\n"
		  "2. Insertion Sort\n\n"
		  "Select an option with the number in front of it")

	choice = int(input("> "))

	if choice == 1:
		BubbleSort(Array)
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

# Main container for running functions
if __name__ ==  "__main__":
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

