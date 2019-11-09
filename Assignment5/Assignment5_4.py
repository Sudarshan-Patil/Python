global no
sum = 0
def calculate():	
	global no, sum
	if (no != 0):
		sum = sum + no%10
		no = int(no/10)			
		calculate()
		
def main():
	global no
	no = int(input("Enter the number : "))
	calculate()
	print("Addition of digits : ", sum)

if (__name__ == "__main__"):
	main()