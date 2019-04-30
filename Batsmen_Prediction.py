# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:08:56 2019

@author: Vivek
"""

# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the Batsmen Dataset
dataset = pd.read_csv('Batsmen\Batsmen.csv')
X = dataset.iloc[:, [1, 2, 3, 4, 5, 6]].values

# Using Elbow Method to find the optimal number of Clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=300, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Fitting K-Meaens Clustering Algorithm to the Dataset
kmeans = KMeans(n_clusters=4, init='k-means++', n_init=10, max_iter=300, random_state=0)
y_kmeans = kmeans.fit_predict(X)

# Visualising the Clusters
plt.scatter(X[y_kmeans == 0,3], X[y_kmeans == 0,4], s = 100, c = 'purple', label = 'Average Form')
plt.scatter(X[y_kmeans == 1,3], X[y_kmeans == 1,4], s = 100, c = 'blue', label = 'Good Form')
plt.scatter(X[y_kmeans == 2,3], X[y_kmeans == 2,4], s = 100, c = 'red', label = 'Bad Form')
plt.scatter(X[y_kmeans == 3,3], X[y_kmeans == 3,4], s = 100, c = 'green', label = 'Peek Form')
plt.scatter(kmeans.cluster_centers_[:, 3], kmeans.cluster_centers_[:, 4], s = 150, c = 'cyan', label = 'Centroids')
plt.title('Recent Form of Batsmen Based on their Stats')
plt.xlabel('Runs')
plt.ylabel('Average')
plt.legend()
plt.show()

# Visualising the Batsmen who scored 4 or more Hundreds
d = pd.read_csv('Batsmen\Hundreds.csv')
x = d.iloc[:, 0].values
y = d.iloc[:, 2].values
plt.figure(figsize = (5,5))
plt.barh(x, y, align = 'center', color = ['#1e90ff', '#1e90ff', '#1e90ff', 'purple', 'purple', 'purple', 'red', 'black', 'gold', 'gold', 'lime'])
plt.title('Batsmen who scored 4 or more Hundreds in between 2018 - 2019')
plt.xlabel('100s Scored')
plt.ylabel('Batsmen')
plt.show()

# Visualising the Batsmen based on their total Runs
x = dataset.iloc[:, 0].values
y = dataset.iloc[:, 4].values
plt.figure(figsize = (15, 15))
plt.pie(y, labels = x, autopct = '%.1f%%')
plt.show()

# Predicting the Best Batsman
print("The best Batsman of the Tournament could possibly be: ",
      dataset.loc[dataset.loc[dataset['Innings']>=15,'Average'].idxmax(),'Names'])