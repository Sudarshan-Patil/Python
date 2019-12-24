from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from scipy.spatial import distance
from sklearn.metrics import accuracy_score
from sklearn import tree

def getDist(test_data, train_data):
	return distance.euclidean(test_data, train_data)

class Classifier():
	def fit(self, train_data, train_target):
		self.TrainingData = train_data
		self.Trainingtarget = train_target
	
	def predict(self, test_data):
		prediction = []
		for i in range(len(test_data)):			
			minDistance = self.getMinDistance(test_data[i])
			prediction.append(minDistance)
		return prediction
			
	def getMinDistance(self, testData):
		minDist = getDist(testData, self.TrainingData[0]);
		index = 0;
		for i in range(1,len(self.TrainingData)):
			dist = getDist(testData, self.TrainingData[i])
			if dist < minDist:
				minDist = dist
				index = i		
		return self.Trainingtarget[index]
		
	def getResultWithTree(self, trainingData, trainingTarget, testingData):
		clf = tree.DecisionTreeClassifier()		
		clf.fit(trainingData, trainingTarget)		
		result = clf.predict(testingData)
		
		return result
		