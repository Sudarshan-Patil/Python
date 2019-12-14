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

	listprocess = processDisplay()

	f = open(argv[1], 'w')	
	f.write("List of active processes" + '\n')

	for ele in listprocess:
		f.write('pid : ' + str(ele['pid']))
		f.write(' username : ' + str(ele['username']))
		f.write(' name : ' + str(ele['name']))
		f.write('\n')

	f.close()		

if __name__ == "__main__":
	main()