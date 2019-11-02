n = int(input("Enter the number : "))
i = sum = 0;
while(n>0):
	i = n%10; 
	n=int(n/10);
	sum = sum + i

print("Sum of all digit : ", sum)