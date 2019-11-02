n = int(input("Number of element : "))
print("Elements : ")
ele = list()
add = 0
for i in range(n):
	a = int(input())
	ele.append(a)
	add = add + a

print("List is ", ele)	
print("Addition is : ", add)