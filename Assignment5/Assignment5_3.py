global no
def pattern():	
	global no
	if (no != 0):
		tmp = no%10
		print(no, end=" ")
		no = no-1				
		pattern()
		

def main():
	global no
	no = int(input("Enter the number : "))
	pattern()


if (__name__ == "__main__"):
	main()