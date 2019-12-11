from sys import *
import os

def displayFiles(path, ext):
	flag = os.path.isabs(path)
	print(ext)

	if flag == False:
		path = os.path.abspath(path)

	exists = os.path.isdir(path)
	if exists:
		for folder, subfolder, files in os.walk(path):
			print(folder)
			for file in files:
				if (file.endswith(ext)):
					print("file names are : ", file)

	else:
		print("Invalid path")	


def main():
	if (len(argv) != 3):
		print("Invalid arguments")
	else:
		displayFiles(argv[1], argv[2])

if __name__ == "__main__":
	main()