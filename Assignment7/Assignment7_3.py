from Arithmetic import *
class Number:
	def __init__(self, number):
		self.number = number

	def showResult(self):
		if (ChkPrime(self.number)):
			print("Given number is prime number")
		else:
			print("Given number is not prime number")

		if (ChkPerfect(self.number)):
			print("Given number is a perfect number")
		else:
			print("Given number is not a perfect number")

		print("Factor of given number is : ", factors(self.number))
		print("Sum of factors are : ", sumFactor(self.number))


def main():
	n = int(input("Please enter the number"))
	obj = Number(n)	
	obj.showResult()

if __name__=="__main__":
	main()