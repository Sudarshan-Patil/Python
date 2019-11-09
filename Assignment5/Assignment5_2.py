global no
def pattern():	
	global no
	if (no != 0):
		tmp = no
		no = no-1		
		pattern()
		print(tmp, end=" ")
		
def main():
	global no
	no = int(input("Enter the number : "))
	pattern()

if (__name__ == "__main__"):
	main()