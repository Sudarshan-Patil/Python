from sys import *
import os
import HashModule

def displayFiles(src):
	flag = os.path.isabs(src)
	if flag == False:
		src = os.path.abspath(src)
	exists = os.path.isdir(src)
	if exists:
		for folder, subfolder, files in os.walk(src):	
			for file in files:
				file = os.path.join(folder, file)
				print("File = ", file)
				print("checksum = ", HashModule.checksum(file))
				print("-"*50)
				
	else:
		print("Invalid path")	


def main():
	if (len(argv) != 2):
		print("Invalid arguments")
	else:
		displayFiles(argv[1])

if __name__ == "__main__":
	main()