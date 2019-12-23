from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from scipy.spatial import distance
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn import preprocessing 

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

def main():
	data = load_iris()
	
	label_encoder = preprocessing.LabelEncoder()
	
	raw_data = pd.read_csv('MarvellousInfosystems_PlayPredictor.csv', index_col=0)
# 	
# 	climate = pd.DataFrame(df, index = ['Wether', 'Temperature'])
	
	dataset = pd.read_csv('MarvellousInfosystems_PlayPredictor.csv', sep=',').values
	
	sourcedata = pd.DataFrame(raw_data, columns = ['Wether', 'Temperature'])
	targetdata = pd.DataFrame(raw_data, columns = ['Play'])
			
# 	sourcedata = label_encoder.fit_transform(sourcedata)
	targetdata = label_encoder.fit_transform(targetdata)
	
	print(targetdata)
		
	train_data, test_data, train_target, test_target = train_test_split(sourcedata, targetdata, test_size = 0.5)

	classifier = Classifier()
	
	classifier.fit(train_data, train_target)
	
	result = classifier.predict(test_data)	
	print(result)
	accuracy = accuracy_score(test_target,result)
	print(accuracy*100)

if __name__ == "__main__":
	main()