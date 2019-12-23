import numpy as ny
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.externals.six import StringIO
import pydot

border = "-"*100
classifier = tree.DecisionTreeClassifier()

def displayData(data):
	
	print(border)	
	print("Targets are : ")
	print(data.target_names)
	print(border)	
	print("Features are : ")
	print(data.feature_names)
	print(border)
	
def displayDetails(data):
	print(border)
	print("Load in iris dataset is : ")
	for i in range(len(data.target)):
		print("ID : %d Features : %s Target : %s"%(i, data.data[i], data.target[i]))
	print(border)
	
def calculateDistance(training_data, training_target, testing_data):	
	classifier.fit(training_data, training_target)
	
	return classifier.predict(testing_data)
	
def calculate(dataset,testArr):
	training_data = ny.delete(dataset.data, testArr, axis=0)
	training_target = ny.delete(dataset.target, testArr)
	
	testing_data = dataset.data[testArr]
	testing_target = dataset.target[testArr]
	
	result = calculateDistance(training_data, training_target, testing_data)
	
	return testing_target, result
	

def main():
	dataset = load_iris()
	
	displayData(dataset)
	displayDetails(dataset)
	
	testArr = [0,1,2,50,51,52,100,101,102]
	
	training, result = calculate(dataset,testArr)
	
	print("Training Target : ")
	print(training)
	print(border)
	print("Training Result : ")
	print(result)
	
	dot_data = StringIO()
	
	tree.export_graphviz(classifier, out_file = dot_data, feature_names = dataset.feature_names, class_names = dataset.target_names, filled = True, rounded = True, impurity = False)

	graph = pydot.graph_from_dot_data(dot_data.getvalue())
	
	graph[0].write_pdf("Iris.pdf")

if __name__ == "__main__":
	main()