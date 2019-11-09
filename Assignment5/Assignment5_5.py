global no
fact = 1
def calculate():	
	global no, fact
	if (no != 0):
		fact = fact * no
		no = no-1		
		calculate()
		
def main():
	global no
	no = int(input("Enter the number : "))
	calculate()
	print("Factorial : ", fact)

if (__name__ == "__main__"):
	main()