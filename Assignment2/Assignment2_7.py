def printPattern(n):
	for i in range(n):
		for j in range(1, n+1):
			print(" ", j, end="")
		print("")

n = int(input("Enter the number : "))
printPattern(n)