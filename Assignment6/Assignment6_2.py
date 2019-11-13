class Circle:
	PI=3.14
	def __init__(self):
		self.radius = 0.0
		self.area = 0.0
		self.circumference = 0.0

	def Accept(self, value):
		self.radius = value
	
	def CalculateArea(self):
		self.area = self.PI*self.radius**2

	def CalculateCirecumference(self):
		self.circumference = 2*self.PI*self.radius

	def Display(self):
		print("Radius is ", self.radius)
		print("Area is ", self.area)
		print("Circumference is ", self.circumference)

def main():
	radius = int(input("Enter the radius"))
	obj1 = Circle()
	obj1.Accept(radius)
	obj1.CalculateArea()
	obj1.CalculateCirecumference()
	obj1.Display()

if __name__ == "__main__":
	main()