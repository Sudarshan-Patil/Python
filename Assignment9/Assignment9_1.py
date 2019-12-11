from sys import *
import os


def main():
	print("File Name : " + argv[0])

	if (len(argv) != 2):
		print("Invalid argument")
		exit()
	
	if os.path.isfile(argv[1]):
    		print (argv[1] + " file exist")
	else:
    		print (argv[1] + " file does not exist")

if __name__ == "__main__":
	main()
	