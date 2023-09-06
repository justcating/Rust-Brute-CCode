
maximumNum 	= 	input("Max of numbers (e.g. 100) > ")
firstWord1 	= 	input("First Word 1 (e.g. turret)> ")
firstWord2 	= 	input("First Word 2 (e.g. compound)> ")
firstWord3 	= 	input("First Word 3 (e.g. drone)> ")
firstWord4 	= 	input("First Word 4 (e.g. camera)> ")

fileName	=	input("File Name > ")

with open(fileName, "a") as file:
	#for num in range(int(maximumNum)):
	#	file.write(str(num) + "\n")

	print("Generating...")

	for num in range(int(maximumNum)+2):
		file.write(firstWord1 + str(num) + "\n")

	for num in range(int(maximumNum)):
		file.write(firstWord2 + str(num) + "\n")

	for num in range(int(maximumNum)):
		file.write(firstWord3 + str(num) + "\n")

	for num in range(int(maximumNum)):
		file.write(firstWord4 + str(num) + "\n")

print("\nDone.")