def printStar(n):
	for i in range(n):
		for j in range(n):
			print(" *", end="")
		print("")

n = int(input("Enter number : "))
printStar(n)