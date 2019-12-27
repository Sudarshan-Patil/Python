import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
import numpy as np
from scipy.spatial import distance
from sklearn.neighbors import KNeighborsClassifier

def eucdistance(test, train):
	return distance.euclidean(test, train)

class Classifier:
	def __init__(self, source, target):
		train_data, test_data, train_target, test_target = train_test_split(source, target, test_size=0.3)
		self.trainingData = train_data
		self.trainingTarget = train_target
		self.testingData = test_data
		self.testingTarget = test_target

	def usingDecisionTree(self):
		clf = tree.DecisionTreeClassifier()
		clf.fit(self.trainingData, self.trainingTarget)
		result = clf.predict(self.testingData)
		return result

	def checkAccuracy(self, result):
		accuracy = accuracy_score(self.testingTarget, result)
		return accuracy*100

	def predict(self):
		prediction=[]
		for i in range(len(self.testingData)):
			prediction.append(self.getDistance(self.testingData[i]))
		return prediction

	def usingKnn(self, n=3):
		knn = KNeighborsClassifier(n_neighbors=n)
		knn.fit(self.trainingData, self.trainingTarget)
		result = knn.predict(self.testingData)
		return result

	def getDistance(self, test_data):
		minDistance = 0
		index = 0
		for i in range(len(self.trainingData)):
			distance = eucdistance(test_data, self.trainingData[i])
			if (distance < minDistance):
				minDistance = distance
				index = i
		return self.trainingTarget[i]

def main():
	source = pd.read_csv('WinePredictor.csv', skiprows=[1], usecols = [1,2,3,4,5,6,7,8,9,10,11,12,13])
	target = pd.read_csv('WinePredictor.csv', skiprows=[1], usecols = [0])

	dfsource = pd.DataFrame(source)
	dfsource.columns = dfsource.columns.str.replace(' ', '')
	dfsource.columns = dfsource.columns.str.replace('/', '')

	features = list(zip(source.Alcohol, source.Malicacid, source.Ash, source.Alcalinityofash, source.Magnesium, source.Totalphenols, source.Flavanoids, source.Nonflavanoidphenols, source.Proanthocyanins, source.Colorintensity, source.Hue, source.OD280OD315ofdilutedwines, source.Proline))
	target = list(target.Class)

	classifier = Classifier(features, target)

	result = classifier.usingDecisionTree()

	print("Total Decision tree accuracy : ", classifier.checkAccuracy(result))

	knnresult = classifier.predict()

	print("Total User defined KNN accuracy : ", classifier.checkAccuracy(knnresult))

	for i in range(1, len(classifier.trainingData)):
		knn = classifier.usingKnn(i)
		print("Total KNN accuracy with  n as %d is : %f"% (i, classifier.checkAccuracy(knn)))

if __name__ == "__main__":
	main()