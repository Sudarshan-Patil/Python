from sklearn.externals.six import StringIO
import pydot


dat_data = StringIO()

tree.export_graphviz(clf, out_file = dot_data, feature_names = dataset.feature_names, class_name = dataset.target_names, filled=True, rounded=True, impurity=False)

graph = pydot.graph_from_dot_data(dot_data.getvalue())

graph[0].write_pdf("Marvellous.pdf")