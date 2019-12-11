from sys import *
import os
import shutil

def displayFiles(src, dest):
	flag = os.path.isabs(src)
	if flag == False:
		src = os.path.abspath(src)

	if (os.path.exists(dest) == False):
		os.mkdir(dest)

	dest = os.path.abspath(dest)

	exists = os.path.isdir(src)
	if exists:
		for folder, subfolder, files in os.walk(src):	
			for file in files:
				file = os.path.join(folder, file)
				shutil.copy(file, dest)
					
						
				

	else:
		print("Invalid path")	


def main():
	if (len(argv) != 3):
		print("Invalid arguments")
	else:
		displayFiles(argv[1], argv[2])

if __name__ == "__main__":
	main()