class Demo:
	number = 2
	def __init__(self, num1, num2):
		self.no1 = num1
		self.no2 = num2

	def add(self):
		return self.no1+self.no2
	@classmethod
	def multi(cls):
		return cls.number*cls.number

	@staticmethod
	def stat():
		return "Hello from static"

class New(Demo):
	def __init__(self, num1, num2):
		super().__init__(num1, num2)

	def inc(self):
		return self.number+100

	
def main():
	d=New(10,20)
	print("Addition is ", d.add())
	print("Multiplication is ", New.multi())
	print("From stat method is ", New.stat())
	print("From New method is ", d.inc())

if __name__ == "__main__":
	main()
		