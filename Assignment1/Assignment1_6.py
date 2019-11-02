def checkNum(n):
	if (n > 0):
		print(n, " is a positive number")
	elif(n < 0):
		print(n, " is a negative number")
	else:
		print(n, " is a zero");

n = int(input("Enter any number : "))
checkNum(n)