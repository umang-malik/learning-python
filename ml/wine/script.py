import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
df = pd.read_csv('wine.data', names = ['class','x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','x11','x12','x13'])
# pd.plotting.scatter_matrix(df);
# plt.show()

X = df.values[:,1:13]
Y = df.values[:,0]
trainX, testX, trainY, testY = train_test_split( X, Y, test_size = 0.3 )

logistic = LogisticRegression()
logistic.fit(trainX,trainY)
print('Logistic Regression Score: \n', logistic.score(testX, testY))

neighbors = KNeighborsClassifier(n_neighbors=7)
neighbors.fit(trainX, trainY)
print('KNN Score: \n', neighbors.score(testX, testY))

decision = DecisionTreeClassifier(criterion='gini')
decision.fit(trainX,trainY)
print('Decision Tree Score: \n', decision.score(testX,testY))
