def ChkPrime(num):
	for i in range(2,num):
		if (num%i == 0):
			return False
	return True

def ChkPerfect(num):
	perfect = 0;
	for i in range(1, num):
		if (num%i == 0):
			perfect = perfect + i
	if (perfect == num):
		return True
	else:
		return False

def factors(num):
	fact = ''
	for i in range(1, num):
		if (num%i == 0):
			fact = fact + str(i) 
	return fact

def sumFactor(num):
	sumfact = 0
	for i in range(1, num):
		if (num%i == 0):
			sumfact = sumfact + i  
	return sumfact