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

# Iniatilising the Variables to '0'
Ind1 = Ind2 = Ind3 = Ind4 = Ind5 = Ind6 = Ind7 = Ind8 = 0
Sa = Eng = Wi = Aus = Nz = Pak = Ban = Afg = 0

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
d = pd.read_csv('Teams\World Cup Stats.csv')
x = d.iloc[:, 0].values
y = d.iloc[:, [2, 3]].values

AUS = SA = IND = ENG = PAK = WI = NZ = SL = 0
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
        b1 = Button(frame, text="India's Wins Against Other Nations Since 2018", command=plot_india_wins, highlightbackground="green", fg="white").pack(side = LEFT)
        b2 = Button(frame, text="Winning Probabilties for Teams", command=plot_win_percentage, highlightbackground="blue", fg="white").pack(side = LEFT)
        b3 = Button(bottomframe, text="Stop", command=root.destroy, highlightbackground="red", fg="white").pack(side = BOTTOM)
        
    else: # If you are using either Windows or Linux
        b1 = Button(frame, text="India's Wins Against Other Nations Since 2018", command=plot_india_wins, bg="green", fg="white").pack(side = LEFT)
        b2 = Button(frame, text="Winning Probabilities for Various Teams", command=plot_win_percentage, bg="blue", fg="white").pack(side = LEFT)
        b3 = Button(bottomframe, text="Stop", command=root.destroy, bg="red", fg="white").pack(side = BOTTOM)

    root.mainloop()

if __name__ == '__main__':
    app()