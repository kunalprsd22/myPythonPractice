import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn import tree

# Decision tree:
# As a first approximation, we will say that it is an object that,
# given several instances with a given set of features X and a given
# set of target labels y, the decision tree automatically learns rules
# (from most to least important) about each feature in order to decide
# which label corresponds to each instance.
#
# Let's separate the Titanic dataset into:
#
# 1. An X variable with the attributes you will use to predict.
#
# 2. A y variable with the label you want to predict.
#    In this case, whether the passenger survived or not.


df = pd.read_csv('DataSet_Titanic.csv')
#print(df.head())


# store in variable X the predictor attributes (all the labels except "Survivor")
X = df.drop('Survivor', axis=1)

# store in y the label to predict ("Survivor")
Y = df.Survivor

# We create a tree object
my_tree = DecisionTreeClassifier(max_depth=2, random_state=42)

# we train the machine
my_tree.fit(X, Y)

# We predict on our set
prediction_y = my_tree.predict(X)

# We compare with the real labels
print("Accuracy: ", accuracy_score(prediction_y, Y))

# we create a confusion matrix
cm = confusion_matrix(Y, prediction_y)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)

disp.plot(cmap=plt.cm.Blues, values_format='.0f')
#plt.show()

# we show a tree graphically
plt.figure(figsize= (10, 8))
tree.plot_tree(my_tree, filled= True, feature_names= X.columns)
plt.show()