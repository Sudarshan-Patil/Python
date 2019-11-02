from functools import reduce

def FilterNum(n1):
	status = True
	for i in range(2, n1):
		if (n1%i == 0):
			status = False
	return status

def MapNum(n1):
	return n1 * 2

def ReduceNum(n1, n2):
	if (n1 > n2):
		return n1
	else:
		return n2

ele = list()
n = int(input("Enter the limit : "))
print("Elements : ")
for i in range(n):
	num = int(input())
	ele.append(num)

print("Input List : ", ele)
filteredEle = list(filter(FilterNum, ele))
print("List after filter : ", filteredEle)
mappedEle= list(map(MapNum, filteredEle))
print("List after map : ", mappedEle)
res = reduce(ReduceNum, mappedEle)
print("Output of reduce : ", res)