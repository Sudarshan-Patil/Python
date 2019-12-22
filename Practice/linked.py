class Node:
	def __init__(self, value):
		self.data = value
		self.next = None


class LinkedList:
	def __init__(self):
		self.start = None
		
	def insert(self, value, pos=0):
		newNode = Node(value)		
		if self.start == None:
			self.start = newNode
		else:
			tmp = self.start
			cur = 1
			while(cur < pos):
				tmp = tmp.next
				cur = cur+1
				if (tmp.next == None):
					break
				
			newNode.next = tmp.next
			tmp.next = newNode

	def view(self):
		tmp = self.start
		while (tmp != None):
			print(tmp.data, end=" ")
			tmp =tmp.next

	def remove(self, pos):
		if (self.start == None):
			print("Linkedlist is empty")
		else:
			tmp = self.start
			cur = 1
			nopos = False
			while (tmp != None):
				if (cur == pos):
					break
					nopos = True

				tmp = tmp.next
				cur = cur + 1
					
			if (nopos != True):
				tmp.next = tmp.next.next
			else:
				print("No position found")


ll = LinkedList()
ll.insert(10)
ll.insert(11)
ll.insert(12)
ll.insert(13)
ll.insert(14)
ll.insert(15)
ll.insert(16)
ll.view()
print("")
n = int(input("Delete from position"))
ll.remove(n)
ll.view()