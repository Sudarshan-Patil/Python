class Arithmetic:	
	def __init__(self):
		self.value1 = 0
		self.value2 = 0
		
	def Accept(self, value1, value2):
		self.value1 = value1
		self.value2 = value2
	
	def Addition(self):
		return self.value1 + self.value2

	def subtraction(self):
		return self.value1 - self.value2

	def Multiplication(self):
		return self.value1 * self.value2

	def Division(self):
		return self.value1/self.value2

def main():
	no1 = int(input("Enter the number 1 : "))
	no2 = int(input("Enter the number 2 : "))
	
	obj1 = Arithmetic()
	obj1.Accept(no1, no2)
	print("Addtion is ", obj1.Addition())
	print("Subtraction is ", obj1.subtraction())
	print("Multiplication is ", obj1.Multiplication())
	print("Division is ", obj1.Division())
	
if __name__ == "__main__":
	main()