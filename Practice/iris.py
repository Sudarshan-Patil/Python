import numpy as ny
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.externals.six import StringIO
import pydot

dataset = load_iris()

print("Target in iris : ")
print(dataset.target_names)

print("Feature in iris : ")
print(dataset.feature_names)

for i in range(len(dataset.data)):
    print("ID : %d Label : %s Feature : %s"%(i, dataset.data[i], dataset.target[i]))


testArr = [0, 50, 100]

train_target = ny.delete(dataset.target, testArr)
train_data = ny.delete(dataset.data, testArr, axis=0)

test_target = dataset.target[testArr]
test_data = dataset.data[testArr]

clf = tree.DecisionTreeClassifier()

clf.fit(train_data, train_target)

res = clf.predict(test_data)

print(test_target)
print(res)

dot_data = StringIO()

tree.export_graphviz(clf, out_file = dot_data, feature_names = dataset.feature_names, class_names = dataset.target_names, filled=True, rounded=True, impurity=False)

graph = pydot.graph_from_dot_data(dot_data.getvalue())

graph[0].write_pdf("Marvellous.pdf")