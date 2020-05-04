
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('creditcard.csv')
X = dataset.iloc[:, 1:30].values
y = dataset.iloc[:, 30].values


#-------Splitting the dataset to training set and test set----------------
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


#----------Feature scaling----------------------------------
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#-------Applying Random Forest Classifier----------------------------
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 100, random_state = 0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

Accuracy_of_testset = ((cm[0, 0] + cm[1, 1])/(cm[0, 0] + cm[1, 1] + cm[0, 1] + cm[1, 0]))*100

y_train_pred = classifier.predict(X_train)

from sklearn.metrics import accuracy_score
Accuracy_of_trainingset = accuracy_score(y_train, y_train_pred)*100

