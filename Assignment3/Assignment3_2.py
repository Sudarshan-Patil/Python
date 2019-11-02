n = int(input("Number of element : "))
print("Elements : ")
ele = list()
for i in range(n):
	a = int(input())
	ele.append(a)
print("List is ", ele)	
for i in range(1, n):
	if (ele[i-1] > ele[i]):
		ele[i] = ele[i-1]	

	
print("maximum number is : ", ele[n-1])