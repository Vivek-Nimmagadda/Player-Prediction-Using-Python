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
plt.figure(figsize = (10, 10))
plt.bar(Names, Teams, color = ['#1e90ff', 	'#228b22'])
plt.bar(Names1, Teams1, color = ['#1e90ff', 'purple'])
plt.bar(Names2, Teams2, color = ['#1e90ff', 'red'])
plt.bar(Names3, Teams3, color = ['#1e90ff', 'gold'])
plt.bar(Names4, Teams4, color = ['#1e90ff', 'black'])
plt.bar(Names5, Teams5, color = ['#1e90ff', 'lime'])
plt.bar(Names6, Teams6, color = ['#1e90ff', '#006400'])
plt.bar(Names7, Teams7, color = ['#1e90ff', 'blue'])
plt.title('Total Wins for India over other Countries in between (2018 - 2019)')
plt.xlabel('Teams')
plt.ylabel('No. of Wins')                                 