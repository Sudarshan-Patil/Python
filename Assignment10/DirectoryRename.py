from sys import *
import os

def displayFiles(path, oldext, newext):
	flag = os.path.isabs(path)

	if flag == False:
		path = os.path.abspath(path)

	exists = os.path.isdir(path)
	if exists:
		for folder, subfolder, files in os.walk(path):	
			for file in files:
				if (file.endswith(oldext)):
					print(folder)
					file = os.path.join(folder, file)
					base = os.path.splitext(file)[0]
					os.rename(file, base + newext)
						
				

	else:
		print("Invalid path")	


def main():
	if (len(argv) != 4):
		print("Invalid arguments")
	else:
		displayFiles(argv[1], argv[2], argv[3])

if __name__ == "__main__":
	main()