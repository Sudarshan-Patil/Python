from functools import reduce

def FilterNum(n1):
	if (n1 >= 70 and n < 90 ):
		return True
	else:
		return False

def MapNum(n1):
	return n1 + 10

def ReduceNum(n1, n2):
	return n1 * n2


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