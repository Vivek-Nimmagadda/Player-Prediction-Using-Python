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
dataset = pd.read_csv('Teams\India.csv')

# First Column is for India and the Second one is for the Country which faced India since 2018
Names = ['IND1', 'SA']
Names1 = ['IND2', 'ENG']
Names2 = ['IND3', 'WI']
Names3 = ['IND4', 'AUS']
Names4 = ['IND5', 'NZ']
Names5 = ['IND6', 'PAK']
Names6 = ['IND7', 'BAN']
Names7 = ['IND8', 'AFG']

# Storing the Total No of Wins which faced against India since 2018 in their respective Variables
Ind1 = ((dataset['Opponent'] == 'South Africa') & (dataset['Result'] == 'Won')).sum()
Sa = ((dataset['Opponent'] == 'South Africa') & (dataset['Result'] == 'Lost')).sum()

Ind2 = ((dataset['Opponent'] == 'England') & (dataset['Result'] == 'Won')).sum()
Eng = ((dataset['Opponent'] == 'England') & (dataset['Result'] == 'Lost')).sum()

Ind3 = ((dataset['Opponent'] == 'West Indies') & (dataset['Result'] == 'Won')).sum()
Wi = ((dataset['Opponent'] == 'West Indies') & (dataset['Result'] == 'Lost')).sum()

Ind4 = ((dataset['Opponent'] == 'Australia') & (dataset['Result'] == 'Won')).sum()
Aus = ((dataset['Opponent'] == 'Australia') & (dataset['Result'] == 'Lost')).sum()

Ind5 = ((dataset['Opponent'] == 'New Zealand') & (dataset['Result'] == 'Won')).sum()
Nz = ((dataset['Opponent'] == 'New Zealand') & (dataset['Result'] == 'Lost')).sum()

Ind6 = ((dataset['Opponent'] == 'Pakistan') & (dataset['Result'] == 'Won')).sum()
Pak = ((dataset['Opponent'] == 'Pakistan') & (dataset['Result'] == 'Lost')).sum()

Ind7 = ((dataset['Opponent'] == 'Bangladesh') & (dataset['Result'] == 'Won')).sum()
Ban = ((dataset['Opponent'] == 'Bangladesh') & (dataset['Result'] == 'Lost')).sum()

Ind8 = ((dataset['Opponent'] == 'Afghanistan') & (dataset['Result'] == 'Won')).sum()
Afg = ((dataset['Opponent'] == 'Afghanistan') & (dataset['Result'] == 'Lost')).sum()

# Storing Variables as Lists for Visualization
Teams = [Ind1, Sa]
Teams1 = [Ind2, Eng]
Teams2 = [Ind3, Wi]
Teams3 = [Ind4, Aus]
Teams4 = [Ind5, Nz]
Teams5 = [Ind6, Pak]
Teams6 = [Ind7, Ban]
Teams7 = [Ind8, Afg]

# Visualising India's Wins over other Countries since 2018
def plot_india_wins():
    global ax
    global graph
    
    ax.cla()
    ax.grid()
    ax.bar(Names, Teams, color = ['#1e90ff', 	'#228b22'])
    ax.bar(Names1, Teams1, color = ['#1e90ff', 'purple'])
    ax.bar(Names2, Teams2, color = ['#1e90ff', 'red'])
    ax.bar(Names3, Teams3, color = ['#1e90ff', 'gold'])
    ax.bar(Names4, Teams4, color = ['#1e90ff', 'black'])
    ax.bar(Names5, Teams5, color = ['#1e90ff', 'lime'])
    ax.bar(Names6, Teams6, color = ['#1e90ff', '#006400'])
    ax.bar(Names7, Teams7, color = ['#1e90ff', 'blue'])
    ax.set_title('Total Wins for India over other Countries in between (2018 - 2019)')
    ax.set_xlabel('Teams')
    ax.set_ylabel('No. of Wins')
    graph.draw()
 
# Fetching World Cup Stats of the Top 8 Teams
d = pd.read_csv('Teams\World Cup Team Records.csv')
x = d.iloc[:, 0].values
y = d.iloc[:, [2, 3]].values

Top_Teams = []
for index, row in d.iterrows():
    if(index == 0):
        AUS = (row['Won'] / row['Lost'])
    elif(index == 1):
        SA = (row['Won'] / row['Lost'])
    elif(index == 2):
        IND = (row['Won'] / row['Lost'])
    elif(index == 3):
        ENG = (row['Won'] / row['Lost'])
    elif(index == 4):
        PAK = (row['Won'] / row['Lost'])
    elif(index == 5):
        WI = (row['Won'] / row['Lost'])
    elif(index == 6):
        NZ = (row['Won'] / row['Lost'])
    else:
        SL = (row['Won'] / row['Lost'])
Top_Teams = [AUS, SA, IND, ENG, PAK, WI, NZ, SL]

# Importing the Training Dataset
d1 = pd.read_csv('Teams\World Cup Match Results Train.csv')
X1_train = d1.iloc[:, [0, 2, 3]].values
Y1_train = d1.iloc[:, [1, 2, 3]].values
Z1_train = d1.iloc[:, [2, 3]].values
Out1_train = d1.iloc[:, 4].values

# Comverting the Categorical Data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
X1_train[:, 0] = labelencoder.fit_transform(X1_train[:, 0])
Y1_train[:, 0] = labelencoder.fit_transform(Y1_train[:, 0])

# Encoding the Dummy Variables
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
X1_train = onehotencoder.fit_transform(X1_train).toarray()
Y1_train = onehotencoder.fit_transform(Y1_train).toarray()
X1_train = np.delete(X1_train, np.s_[8:12], axis=1)
Y1_train = np.delete(Y1_train, np.s_[8:12],axis=1)
X1_train = np.concatenate((X1_train, Y1_train),axis=1)
X1_train = np.concatenate((X1_train, Z1_train),axis=1)

# Fitting Logistic Regression to the Training Set
from sklearn.linear_model import LogisticRegression
classifier_LR = LogisticRegression()
classifier_LR.fit(X1_train, Out1_train)

# Fitting SVM to the Training Set
from sklearn.svm import SVC
classifier_SVC = SVC()
classifier_SVC.fit(X1_train, Out1_train)

# Fitting K-Nearest Neighbors Algorithm to the Training Set
from sklearn.neighbors import KNeighborsClassifier
classifier_KNN = KNeighborsClassifier(n_neighbors = 10, metric = 'minkowski', p = 2)
classifier_KNN.fit(X1_train, Out1_train)

# Fitting Naive Bayes to the Training Set
from sklearn.naive_bayes import GaussianNB
classifier_GNB = GaussianNB()
classifier_GNB.fit(X1_train, Out1_train)

# Fitting Decision trees to the Training Set
from sklearn.tree import DecisionTreeClassifier
classifier_DT = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier_DT.fit(X1_train, Out1_train)

# Fitting Random Forest to the Training Set
from sklearn.ensemble import RandomForestClassifier
classifier_RF = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state = 0)
classifier_RF.fit(X1_train, Out1_train)

# Importing the Testing Dataset
d2 = pd.read_csv('Teams\World Cup Match Results Test.csv')
X1_test = d2.iloc[:, [0, 2, 3]].values
Y1_test = d2.iloc[:, [1, 2, 3]].values
Z1_test = d2.iloc[:, [2, 3]].values
Out1_test = d2.iloc[:, 4].values

# Converting the Categorical Data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
X1_test[:, 0] = labelencoder.fit_transform(X1_test[:, 0])
Y1_test[:, 0] = labelencoder.fit_transform(Y1_test[:, 0])

# Encoding the Dummy Variables
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
X1_test = onehotencoder.fit_transform(X1_test).toarray()
Y1_test = onehotencoder.fit_transform(Y1_test).toarray()
X1_test = np.delete(X1_test, np.s_[8:12], axis=1)
Y1_test = np.delete(Y1_test, np.s_[8:12],axis=1)
X1_test = np.concatenate((X1_test, Y1_test),axis=1)
X1_test = np.concatenate((X1_test, Z1_test),axis=1)

# Predicting the Test Set Results for various Classification Techniques
Out1_pred_LR = classifier_LR.predict(X1_test)
Out1_pred_SVC = classifier_SVC.predict(X1_test)
Out1_pred_KNN = classifier_KNN.predict(X1_test)
Out1_pred_GNB = classifier_GNB.predict(X1_test)
Out1_pred_DT = classifier_DT.predict(X1_test)
Out1_pred_RF = classifier_RF.predict(X1_test)

# Creating the Confusion Matrices for various Classification Techniques
from sklearn.metrics import confusion_matrix
cm_LR = confusion_matrix(Out1_test, Out1_pred_LR)
cm_SVC = confusion_matrix(Out1_test, Out1_pred_SVC)
cm_KNN = confusion_matrix(Out1_test, Out1_pred_KNN)
cm_GNB = confusion_matrix(Out1_test, Out1_pred_GNB)
cm_DT = confusion_matrix(Out1_test, Out1_pred_DT)
cm_Rf = confusion_matrix(Out1_test, Out1_pred_RF)

# Printing the Win Percentages of Home Teams on the Screen
def facts():
    home_wins = ((d1['Home1'] == 1) & (d1['Won'] == 1)).sum()
    home_losses = ((d1['Home1'] == 1) & (d1['Won'] == 0)).sum()
    home_win_percentage1 = round(((home_wins)/(home_wins + home_losses)) * 100, 1)
    home_wins = ((d2['Home1'] == 1) & (d2['Won'] == 1)).sum()
    home_losses = ((d2['Home1'] == 1) & (d2['Won'] == 0)).sum()
    home_win_percentage2 = ((home_wins)/(home_wins + home_losses)) * 100
    message1 = ("The Win Percentage for Host Team until 2011 World Cup was: ")
    message2 = ("But, during the 2019 World Cup it was a whopping: ")
    canvas_width = 500
    canvas_height = 500
    root = Toplevel()
    root.geometry("700x600")
    root.title("Win Percentage")
    canvas = Canvas(root, width=canvas_width, height=canvas_height)
    canvas.create_text(1, 10, anchor=W, text=message1)
    canvas.create_text(410, 10, anchor=W, text=home_win_percentage1, font='bold')
    canvas.create_text(1, 30, anchor=W, text=message2)
    canvas.create_text(350, 30, anchor=W, text=home_win_percentage2, font='bold')
    canvas.pack()
    root.mainloop()
    
# Importing the 2019 World Cup Schedule Dataset
d3 = pd.read_csv('Teams\World Cup 2019 Schedule.csv')
d4 = pd.read_csv('Teams\World Cup Match Results (1975 - 2015).csv')
X2_train = d4.iloc[:, [0, 2, 3]].values
Y2_train = d4.iloc[:, [1, 2, 3]].values
Z2_train = d4.iloc[:, [2, 3]].values
Out2_train = d4.iloc[:, 4].values

# Converting the Categorical Data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
X2_train[:, 0] = labelencoder.fit_transform(X2_train[:, 0])
Y2_train[:, 0] = labelencoder.fit_transform(Y2_train[:, 0])

# Encoding the Dummy Variables
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
X2_train = onehotencoder.fit_transform(X2_train).toarray()
Y2_train = onehotencoder.fit_transform(Y2_train).toarray()
X2_train = np.delete(X2_train, np.s_[8:12], axis=1)
Y2_train = np.delete(Y2_train, np.s_[8:12],axis=1)
X2_train = np.concatenate((X2_train, Y2_train),axis=1)
X2_train = np.concatenate((X2_train, Z2_train),axis=1)

# Fitting Decision trees to the Training Set
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X2_train, Out2_train)

# Importing the Testing Dataset
X2_test = d3.iloc[:, [0, 2, 3]].values
Y2_test = d3.iloc[:, [1, 2, 3]].values
Z2_test = d3.iloc[:, [2, 3]].values

# Converting the Categorical Data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
X2_test[:, 0] = labelencoder.fit_transform(X2_test[:, 0])
Y2_test[:, 0] = labelencoder.fit_transform(Y2_test[:, 0])

# Encoding the Dummy Variables
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
X2_test = onehotencoder.fit_transform(X2_test).toarray()
Y2_test = onehotencoder.fit_transform(Y2_test).toarray()
X2_test = np.delete(X2_test, np.s_[8:12], axis=1)
Y2_test = np.delete(Y2_test, np.s_[8:12],axis=1)
X2_test = np.concatenate((X2_test, Y2_test),axis=1)
X2_test = np.concatenate((X2_test, Z2_test),axis=1)

# Predicting the Test Set Results for Decision Trees
Out2_pred = classifier.predict(X2_test)

# Visualizing the Win Percentages of the Top 8 Countries Over Each Other     
def plot_win_percentage():
    global ax
    global graph
    
    ax.cla()
    ax.grid()
    ax.bar(x, Top_Teams, color = ['gold', '#228b22', '#1e90ff', 'purple', 'lime', 'red', 'black', 'blue'])
    ax.set_title("Win/Loss Ratio of Top 8 Teams Against Each Other in the World Cups")
    ax.set_xlabel("Teams")
    ax.set_ylabel("Win/Loss Ratio")
    graph.draw()
    
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
    
    if platform.system() == "Darwin": # If you are using a Mac
        b1 = Button(frame, text="India's Wins Since 2018", command=plot_india_wins, highlightbackground="green", fg="white").pack(side = LEFT)
        b2 = Button(frame, text="Winning Probabilties for Teams", command=plot_win_percentage, highlightbackground="blue", fg="white").pack(side = LEFT)
        b3 = Button(frame, text="Host Winning Percentages", command=facts, highlightbackground="#D35400", fg="white").pack(side = LEFT)
        b4 = Button(bottomframe, text="Stop", command=root.destroy, highlightbackground="red", fg="white").pack(side = BOTTOM)
        
    else: # If you are using either Windows or Linux
        b1 = Button(frame, text="India's Wins Against Other Nations Since 2018", command=plot_india_wins, bg="green", fg="white").pack(side = LEFT)
        b2 = Button(frame, text="Winning Probabilities for Various Teams", command=plot_win_percentage, bg="blue", fg="white").pack(side = LEFT)
        b3 = Button(frame, text="Host Winning Percentages", command=facts, bg="#D35400", fg="white").pack(side = LEFT)
        b4 = Button(bottomframe, text="Stop", command=root.destroy, bg="red", fg="white").pack(side = BOTTOM)

    root.mainloop()

if __name__ == '__main__':
    app()