# -*- coding: utf-8 -*-
"""ML_lab_4_bagging.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/157y-cnI4SxwiqhssSbqSxv28s40e5Ww2

Import statements
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Importing dataset"""

df=pd.read_csv("diabetes.csv")

df.head()

df.isnull().any()

df.isnull()

df.describe()

df.drop("SkinThickness",axis=1)

df

df.drop("SkinThickness",axis=1,inplace=True)

df

df1=df.sample(frac=0.5)

df1

df1.describe()

df1.isnull()

X = df1.iloc[:, :-1].values
y = df1.iloc[:, -1].values

"""Splitting datasets into training and testing"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train= sc.fit_transform(X_train)
X_test= sc.transform(X_test)

"""Standardization"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier

dc = DecisionTreeClassifier()
model = BaggingClassifier(estimator= dc, n_estimators=10)
classifiers = model.fit(X_train, y_train)

y_pred = model.predict(X_test)
from sklearn.metrics import accuracy_score

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)