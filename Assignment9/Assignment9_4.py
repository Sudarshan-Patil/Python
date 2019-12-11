from sys import *
import filecmp

def main():
	if (len(argv) != 3):
		print("Invalid argument")
		exit()
	
	if filecmp.cmp(argv[1], argv[2]):
		print("Success")
	else:
		print("Failure")	

if __name__ == "__main__":
	main()
	