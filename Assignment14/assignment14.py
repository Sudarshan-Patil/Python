from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class CheckWeather():
	def __init__(self, sourcedata, targetdata):
		self.sourcedata = sourcedata
		self.targetdata = targetdata
		
	def getTrainingData(self):
		return train_test_split(self.sourcedata, self.targetdata, test_size = 0.5)
		
	def checkAccuracyWithKnn(self, knn=3):
		train_data, test_data, train_target, test_target = self.getTrainingData()
		
		classifierKnn = KNeighborsClassifier(n_neighbors=knn)
		classifierKnn.fit(train_data, train_target)	
		knnresult = classifierKnn.predict(test_data)

		accuracy = accuracy_score(test_target,knnresult)
		print("KNN accuracy : ", accuracy*100)
	
	def checkAccuracyWithTree(self):
		train_data, test_data, train_target, test_target = self.getTrainingData()
		
		classifierTree = tree.DecisionTreeClassifier()
		classifierTree.fit(train_data, train_target)
		treeResult = classifierTree.predict(test_data)
		
		accuracy = accuracy_score(test_target,treeResult)
		print("Tree accuracy : ", accuracy*100)
	
	def checkWeather(self, source):
		classifierTree = tree.DecisionTreeClassifier()
		classifierTree.fit(self.sourcedata, self.targetdata)
		treeResult = classifierTree.predict(source)
		return treeResult
		

def main():
	weatherArr = {'overcast': 0, 'rainy':1, 'sunny':2}
	temperatureArr = {'cool': 0, 'hot':1, 'mild':2}

	label_encoder = preprocessing.LabelEncoder()
		
	sourcedata = pd.read_csv('MarvellousInfosystems_PlayPredictor.csv', usecols = [1,2])
	targetdata = pd.read_csv('MarvellousInfosystems_PlayPredictor.csv', usecols = [3])	
		
	
	sourcedata['Weather'] = label_encoder.fit_transform(sourcedata['Weather'])
	sourcedata['Temperature'] = label_encoder.fit_transform(sourcedata['Temperature'])

	targetdata['Play'] = label_encoder.fit_transform(targetdata['Play'])
	ck = CheckWeather(sourcedata, targetdata)
	
	ck.checkAccuracyWithKnn(3)
	
	ck.checkAccuracyWithTree()
	
	weather = input("Is it Sunny, Rainy or Overcast : ")
	if weather.lower() not in weatherArr:
		print("Invalid weather");
		exit()

	temparature = input("Is it Hot, Mild or Cool : ")
	if temparature.lower() not in temperatureArr:
		print("Invalid temparature");
		exit()
	
	df = [{'Weather' : weatherArr[weather.lower()], 'Temperature' : temperatureArr[temparature.lower()]}]
	data = pd.DataFrame(df)
	
	result = ck.checkWeather(data)
	
	if(result[0]):
		print("Weather is clear for play")
	else:
		print("Sorry, we can play today due to weather")
	
if __name__ == "__main__":
	main()