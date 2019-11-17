from threading import *
from os import *

def Even():
	print("PID of Even process : ", getpid())
	i=1;
	while(i<=20):
		if (i%2==0):
			print(i)
		i = i+1

def Odd():
	print("PID of Odd process : ", getpid())
	i=1;
	while(i<=20):
		if (i%2!=0):
			print(i)
		i = i+1

def main():
	print("PID of main process : ", getpid())
	t1 = Thread(target=Even)
	t1.start()
	t2 = Thread(target=Odd)
	t2.start()

if __name__ == "__main__":
	main()
	