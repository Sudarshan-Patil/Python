from threading import *
from os import *

def small(str):
	print("PID of small process : ", getpid())
	sum = 0
	for i in range(len(str)):	
		if (str[i].islower()):
			sum = sum + 1
	print(sum)
def capital(str):
	print("PID of capital process : ", getpid())
	sum = 0
	for i in range(len(str)):
		if (str[i].isupper()):
			sum = sum + 1
	print(sum)

def digit(str):
	print("PID of digit process : ", getpid())
	sum = 0
	for i in range(len(str)):
		if (str[i].isdigit()):
			sum = sum + 1
	print(sum)
	
def main():
	print("PID of main process : ", getpid())
	str = "aBcDeFG2341"
	t1 = Thread(target=small, args=(str,))
	t1.start()
	t2 = Thread(target=capital, args=(str,))
	t2.start()
	t3 = Thread(target=digit, args=(str,))
	t3.start()
	print("Exit from main")

if __name__ == "__main__":
	main()
	