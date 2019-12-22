from sys import *
import os

path = argv[1]
flag = os.path.isabs(path)

if flag == false:
	path = os.path.abspath(path)

exists = os.path.isdir(path)

if exists:
	for folder, subfolder, files IN os.walk(path):
		print("Current directory : ", folder)
		for subf in subfolder:
			print("Sub folders are : ", subf)
		for file in files:
			print("file names are : ", file)

else:
	print("Invalid path")	