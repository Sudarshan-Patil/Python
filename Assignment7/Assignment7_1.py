class BookStore:
	NoOfBook=0
	def __init__(self, name, author):
		self.name = name
		self.author = author
		BookStore.NoOfBook = BookStore.NoOfBook + 1

	def Display(self):
		
		print(self.name, " No of books : ", BookStore.NoOfBook)

def main():
	obj1 = BookStore("Linux System Programming", "Robert Love")
	obj1.Display()
	
	obj2 = BookStore("C Programming", "Dennis Ritchie")
	obj2.Display()
	
if __name__ == "__main__":
	main()