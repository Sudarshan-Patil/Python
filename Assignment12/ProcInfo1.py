import psutil	
from sys import *

def processDisplay():
	listprocess=[]
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
			listprocess.append(pinfo)
		except:
			pass
	return listprocess		

def main():
	if (len(argv) != 2):
		print("Invalid arguments")
		exit()	

	print("List of active processes")
	listprocess = processDisplay()
	
	for ele in listprocess:
		if argv[1] in ele['name']:
			print(ele)

if __name__ == "__main__":
	main()