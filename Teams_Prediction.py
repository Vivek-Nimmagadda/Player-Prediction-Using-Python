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

Ind = 0
SA = 0

if(dataset.loc[(dataset['Opponent']) == 'South Africa' & (dataset['Result']) == 'Won']):
    Ind = Ind + 1
else:
    SA = SA + 1