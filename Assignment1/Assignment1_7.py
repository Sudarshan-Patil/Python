def ChkNum(n):
	if (n%5 == 0):
		return True
	else:
		return False

n = int(input("Enter number : "))
print(ChkNum(n))