from threading import *
from os import *

def EvenFactor(no):
	print("PID of Even process : ", getpid())
	sum = 0
	for i in range(no):	
		if (i%2==0):
			sum = sum + i
	print(sum)
def OddFactor(no):
	print("PID of Odd process : ", getpid())
	sum = 0
	for i in range(no):
		if (i%2!=0):
			sum = sum + i
	print(sum)
	
def main():
	print("PID of main process : ", getpid())
	t1 = Thread(target=EvenFactor, args=(20,))
	t1.start()
	t2 = Thread(target=OddFactor, args=(20,))
	t2.start()
	print("Exit from main")

if __name__ == "__main__":
	main()
	