from sys import *
import os

def getFrequency(filename, str):
	f = open(filename, 'r')
	content = f.read()
	cnt = content.count(str)
	f.close()
	print(cnt)

def main():
	print("File Name : " + argv[1])
	#print("Frequency of word " + argv[2] + " in file" + argv[1] + " is " + getFrequency(argv[0], argv[1]))
	getFrequency(argv[0], argv[1])

if __name__ == "__main__":
	main()