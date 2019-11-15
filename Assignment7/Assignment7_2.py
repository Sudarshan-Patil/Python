class BankAccount:
	ROI=10.5
	def __init__(self, name, amount):
		self.name = name
		self.amount = amount

	def Display(self):
		print("Name : ", self.name)
		print("Amount : ", self.amount)
	
	def Deposit(self, amount):
		self.amount = self.amount + amount

	def Withdraw(self, amount):
		self.amount = self.amount - amount

	def CalculateInterest(self):
		self.amount = self.amount + self.amount * BankAccount.ROI/100

def main():
	obj1 = BankAccount("A", 1000)
	obj1.Deposit(500)
	obj1.Withdraw(100)
	obj1.CalculateInterest()
	obj1.Display()	

	obj2 = BankAccount("B", 2000)
	obj2.Deposit(500)
	obj2.Withdraw(100)
	obj2.CalculateInterest()
	obj2.Display()

if __name__ == "__main__":
	main()