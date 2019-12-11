from sys import *
import os
import HashModule
from time import *

def displayFiles(src):
	arr = {}
	flag = os.path.isabs(src)
	if flag == False:
		src = os.path.abspath(src)
	fd = open('log.txt', 'w')
	exists = os.path.isdir(src)
	if exists:
		strtime = time()
		for folder, subfolder, files in os.walk(src):	
			for file in files:
				file = os.path.join(folder, file)
				chksum = HashModule.checksum(file)
				if (chksum in arr):
					arr[chksum].append(file)
					fd.write("Duplicate file : " + file + "\n")
					os.remove(file)
				else:
					arr[chksum] = [file]
		endtime = time()
		print("Time taken = ", endtime - strtime)			
		fd.close()
	else:
		print("Invalid path")	


def main():
	if (len(argv) != 2):
		print("Invalid arguments")
	else:
		displayFiles(argv[1])

if __name__ == "__main__":
	main()