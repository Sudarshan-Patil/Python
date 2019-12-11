from sys import *
import os

def readfile(filename):
	f = open(filename)
	content = f.read()
	print(content)
	f.close

def main():
	print("File Name : " + argv[0])

	if (len(argv) != 2):
		print("Invalid argument")
		exit()
	
	if os.path.isfile(argv[1]):
    		readfile(argv[1])
	else:
    		print (argv[1] + " file does not exist")

if __name__ == "__main__":
	main()
	