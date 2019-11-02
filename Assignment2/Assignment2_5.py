n = int(input("Enter the number : "))
status = True
for i in range(2, n):
	if (n%i == 0):
		status = False

if (status):
	print("Number is a prime number")
else:
	print("Number is not a prime number")