from MarvellousNum import ChkPrime

def listPrime(ele):
	add = 0;
	for i in range(len(ele)):
		if (ChkPrime(ele[i])):
			add = add + ele[i]	
	return add;

n = int(input("Number of element : "))
ele = list()
count = 0
print("Elements")
for i in range(n):
	a = int(input())
	ele.append(a)

print("Addition is : ", listPrime(ele))