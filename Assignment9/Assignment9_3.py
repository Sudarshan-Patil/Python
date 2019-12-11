from sys import *
import os

def readfile(filename, new):
	oldFile = open(filename)
	content = oldFile.read()
	newFile = open(new, 'w')
	newFile.write(content)
	oldFile.close()
	newFile.close()

def main():

	if (len(argv) != 3):
		print("Invalid argument")
		exit()
	
	if os.path.isfile(argv[1]):
    		readfile(argv[1], argv[2])
	else:
    		print (argv[1] + " file does not exist")

if __name__ == "__main__":
	main()
	