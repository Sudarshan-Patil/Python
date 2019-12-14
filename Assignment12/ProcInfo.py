import psutil	

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
	print("List of active processes")
	listprocess = processDisplay()
	
	for ele in listprocess:
		print(ele)

if __name__ == "__main__":
	main()