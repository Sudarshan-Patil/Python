from threading import *
from os import *

def Evenlist(*no):
	print("PID of Even process : ", getpid())
	sum = 0
	for i in range(len(no)):	
		if (no[i]%2==0):
			sum = sum + no[i]
	print(sum)
def Oddlist(*no):
	print("PID of Odd process : ", getpid())
	sum = 0
	for i in range(len(no)):
		if (no[i]%2!=0):
			sum = sum + no[i]
	print(sum)
	
def main():
	print("PID of main process : ", getpid())
	t1 = Thread(target=Evenlist, args=(1,2,3,4,5,6,7,8,9,10))
	t1.start()
	t2 = Thread(target=Oddlist, args=(1,2,3,4,5,6,7,8,9,10))
	t2.start()
	print("Exit from main")

if __name__ == "__main__":
	main()
	