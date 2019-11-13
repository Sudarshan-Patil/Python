class Demo:
	value=10
	def __init__(self, no1, no2):
		self.num1 = no1
		self.num2 = no2

	def fun(self):
		print("First instance variable is ", self.num1)

	def gun(self):
		print("Second instance variable is ", self.num2)


def main():
	obj1 = Demo(11,21)
	obj2 = Demo(51,101)
	
	obj1.fun()
	obj2.fun()
	obj1.gun()
	obj2.gun()
	

if __name__ == "__main__":
	main()