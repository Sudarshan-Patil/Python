from threading import *
from os import *

def thread1(lock):
	lock.acquire()
	print("PID of thread1 process : ", getpid())
	for i in range(1, 50):
		print(i)
	lock.release()	

def thread2(lock):
	lock.acquire()
	print("PID of thread2 process : ", getpid())
	for i in range(50, 0, -1):
		print(i)
	lock.release()

def main():
	lock = Lock()
	print("PID of main process : ", getpid())
	t1 = Thread(target = thread1,args=(lock,))
	t1.start()
	t2 = Thread(target = thread2,args=(lock,))
	t2.start()

	

if __name__ == "__main__":
	main()
	