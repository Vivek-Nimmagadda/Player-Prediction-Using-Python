# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:16:18 2019

@author: Vivek
"""

# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the Batsmen Dataset
dataset = pd.read_csv('Bowlers\Bowlers.csv')
X = dataset.iloc[:, [1, 2, 3, 4, 5, 6, 7]].values

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
plt.scatter(X[y_kmeans == 0,2], X[y_kmeans == 0,4], s = 100, c = 'blue', label = 'Good Form')
plt.scatter(X[y_kmeans == 1,2], X[y_kmeans == 1,4], s = 100, c = 'purple', label = 'Average Touch')
plt.scatter(X[y_kmeans == 2,2], X[y_kmeans == 2,4], s = 100, c = 'green', label = 'Peek Form')
plt.scatter(X[y_kmeans == 3,2], X[y_kmeans == 3,4], s = 100, c = 'red', label = 'Poor Form')
plt.scatter(kmeans.cluster_centers_[:, 2], kmeans.cluster_centers_[:, 4], s = 150, c = 'cyan', label = 'Centroids')
plt.title('Recent Form of Bowlers Based on their Stats')
plt.xlabel('Wickets')
plt.ylabel('Average')
plt.legend()
plt.show()

# Visualising the Bowlers who picked 3 or more Four-Wicket Hauls
d = pd.read_csv('Bowlers\Four_Fers.csv')
x = d.iloc[:, 0].values
y = d.iloc[:, 4].values
plt.figure(figsize = (5,5))
plt.barh(x, y, align = 'center', color = ['#1e90ff', '#1e90ff', 'Purple', 'Black', 'Gold', 'blue', 'lime', '#0000cd'])
plt.title('Bowlers who picked 3 or more Four Fers in between 2018 - 2019')
plt.xlabel('Four Wicket Hauls')
plt.ylabel('Bowlers')
plt.show()

# Visualising the Bowleres based on their Total Wickets
x = dataset.iloc[:, 0].values
y = dataset.iloc[:, 3].values
plt.figure(figsize = (15,15))
plt.pie(y, labels = x, autopct = '%.1f%%')
plt.show()

# Predicting the Best Bowler(s)
print("The best Bowlers of the Tournament could possibly be: ",
      dataset.loc[dataset.loc[dataset['Wickets']>=25,'Average'].idxmin(),'Names'])
print("The Leading Wicket taker of the Tournament could well be: ", 
      dataset.loc[dataset.loc[dataset['Wickets'].max()],'Names'])