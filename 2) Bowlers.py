# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:16:18 2019

@author: Vivek
"""

# Importing the Libraries
from tkinter import *
from PIL import Image, ImageTk
import platform
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
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
    
# Visualising the Optimal Number of Clusters
def plot_elbow():
    global ax
    global graph

    ax.cla() # Clears an axes
    ax.grid()
    ax.plot(range(1, 11), wcss, marker='o', color='orange')
    ax.set_title('The Elbow Method', fontsize=20)
    ax.set_xlabel('Number of Clusters', fontsize=15)
    ax.set_ylabel('WCSS', fontsize=15)
    graph.draw()
        
# Fitting K-Meaens Clustering Algorithm to the Dataset
kmeans = KMeans(n_clusters=4, init='k-means++', n_init=10, max_iter=300, random_state=0)
y_kmeans = kmeans.fit_predict(X)

 # Visualising the K-Means Clustered Data   
def plot_kmeans():
    global ax
    global graph
    
    ax.cla()
    ax.grid()
    ax.scatter(X[y_kmeans == 0,2], X[y_kmeans == 0,4], s = 100, c = 'blue', label = 'Good Form')
    ax.scatter(X[y_kmeans == 1,2], X[y_kmeans == 1,4], s = 100, c = 'purple', label = 'Average Form')
    ax.scatter(X[y_kmeans == 2,2], X[y_kmeans == 2,4], s = 100, c = 'green', label = 'Peek Form')
    ax.scatter(X[y_kmeans == 3,2], X[y_kmeans == 3,4], s = 100, c = 'red', label = 'Poor Form')
    ax.scatter(kmeans.cluster_centers_[:, 2], kmeans.cluster_centers_[:, 4], s = 150, c = 'cyan', label = 'Centroids')
    ax.set_title('Recent Form of Bowlers Based on their Stats', fontsize=20)
    ax.set_xlabel('Runs', fontsize=15)
    ax.set_ylabel('Average', fontsize=15)
    graph.draw()

# Fetching the Bowlers who Picked 3 or more Four-Wicket Hauls
d = pd.read_csv('Bowlers\Four_Fers.csv')
x = d.iloc[:, 0].values
y = d.iloc[:, 4].values
     
# Visualising the Bowlers who Picked 3 or more Four-Wicket Hauls
def plot_4_fers():
    global ax
    global graph
    
    ax.cla()
    ax.grid()
    ax.barh(x, y, align = 'center', color = ['#1e90ff', '#1e90ff', 'Purple', 'Black', 'Gold', 'blue', 'lime', '#0000cd'])
    ax.set_title('Bowlers who picked 3 or more Four-Wicket Hauls in between 2018 - 2019', fontsize=20)
    ax.set_xlabel('4-Fers Taken', fontsize=15)
    ax.set_ylabel('Bowlers', fontsize=15)
    graph.draw()
    
# Fetching the Bowlers along with their Total Wickets taken in-between 2018-2019
x1 = dataset.iloc[:, 0].values
y1 = dataset.iloc[:, 3].values

# Visualising the Bowlers based on their Total Wickets
def plot_wickets():
    global ax
    global graph
    
    ax.cla()
    ax.grid()
    ax.pie(y1, labels = x1, autopct = '%.1f%%')
    graph.draw()
    
# Predicting the Best Bowler
def plot_best_bowler():
    best_bowler1 = dataset.loc[dataset.loc[dataset['Wickets']>=25, 'Average'].idxmin(),'Names']
    best_bowler2 = dataset.loc[dataset['Wickets'].idxmax(), 'Names']
    message = ("The best Bowlers of the Tournament could possibly be: " + best_bowler1 + " and " + best_bowler2)
    canvas_width = 500
    canvas_height = 500
    root = Toplevel()
    root.geometry("700x600")
    root.title("Best Bowler")
    canvas = Canvas(root, width=canvas_width, height=canvas_height)
    canvas.create_text(1, 10, anchor=W, text=message)
    img = ImageTk.PhotoImage(Image.open("virat.jpeg"))
    canvas.create_image(0, 20, anchor=NW, image=img)
    canvas.image = img
    canvas.pack()
    root.mainloop()
    
# Fetching the Pacers Data
d1 = pd.read_csv('Bowlers\Fast Bowlers.csv')
x2 = d1.iloc[:, [0, 3, 5, 6, 7]].values
    
# Predicting the Best Pacer
def plot_best_pacer():
    best_pacer = d1.loc[d1.loc[d1['Wickets']>=20, 'Average'].idxmin(), 'Names']
    message = ("The best Pacer of the Tournament could possibly be: " + best_pacer)
    canvas_width = 500
    canvas_height = 500
    root = Toplevel()
    root.geometry("700x600")
    root.title("Best Pacer")
    canvas = Canvas(root, width=canvas_width, height=canvas_height)
    canvas.create_text(1, 10, anchor=W, text=message)
    canvas.pack()
    root.mainloop()
#
    
# Creating a Canvas and a blank Plot using Tkinter
def app():
    global ax
    global graph

    # initialise a window using Tkinter
    root = Tk()
    root.config(background='white')
    root.geometry("1000x800")

    lab = Label(root, text="Graphical Visualization", bg = 'white').pack()

    fig = Figure()

    ax = fig.add_subplot(111)
    ax.set_title('Plain Graph', fontsize=20)
    ax.set_xlabel('x-axis', fontsize=14)
    ax.set_ylabel('y-axis', fontsize=14)
    ax.grid()

    graph = FigureCanvasTkAgg(fig, master=root)
    graph.get_tk_widget().pack(side="top",fill='both',expand=True)

    frame = Frame(root)
    frame.pack()
    bottomframe = Frame(root)
    bottomframe.pack(side = BOTTOM)
    
    # For Background COlors
    if platform.system() == "Darwin": # If you are using a Mac
        b1 = Button(frame, text="Elbow Method", command=plot_elbow, highlightbackground="green", fg="white").pack(side = LEFT)
        b2 = Button(frame, text="K-Means Clustering", command=plot_kmeans, highlightbackground="blue", fg="white").pack(side = LEFT)
        b3 = Button(frame, text="Bowlers who Picked 4 Wicket-Hauls Thrice or more", command=plot_4_fers, highlightbackground="#D35400", fg="white").pack(side = LEFT)
        b4 = Button(frame, text="% of Wickets taken by Players", command=plot_wickets, highlightbackground="#117A65", fg="white").pack(side = LEFT)
        b5 = Button(frame, text="Best Bowlers", command=plot_best_bowler, highlightbackground="#09529C", fg="white").pack(side = LEFT)
        b6 = Button(frame, text="Best Pacer", command=plot_best_pacer, highlightbackground="#34495E", fg="white").pack(side = LEFT)
        b7 = Button(bottomframe, text="Stop", command=root.destroy, highlightbackground="red", fg="white").pack(side = BOTTOM)
        
    else: # If you are using either Windows or Linux
        b1 = Button(frame, text="Elbow Method", command=plot_elbow, bg="green", fg="white").pack(side = LEFT)
        b2 = Button(frame, text="K-Means Clustering", command=plot_kmeans, bg="blue", fg="white").pack(side = LEFT)
        b3 = Button(frame, text="Bowlers who Picked 4 Wicket-Hauls Thrice or more", command=plot_4_fers, bg="#D35400", fg="white").pack(side = LEFT)
        b4 = Button(frame, text="% of Wickets taken by Players", command=plot_wickets, bg="#117A65", fg="white").pack(side = LEFT)
        b5 = Button(frame, text="Best Bowlers", command=plot_best_bowler, bg="#09529C", fg="white").pack(side = LEFT)
        b6 = Button(frame, text="Best Pacer", command=plot_best_pacer, bg="#34495E", fg="white").pack(side = LEFT)
        b7 = Button(bottomframe, text="Stop", command=root.destroy, bg="red", fg="white").pack(side = BOTTOM)

    root.mainloop()

if __name__ == '__main__':
    app()