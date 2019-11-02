n = int(input("Number of element : "))
ele = list()
count = 0
print("Elements")
for i in range(n):
	a = int(input())
	ele.append(a)

search = int(input("Element to search : "))

for i in range(n):
	if (ele[i] == search):
		count = count + 1

print("List is ", ele)
print("Frequency is : ", count)
