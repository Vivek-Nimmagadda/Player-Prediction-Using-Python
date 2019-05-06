World-Cup Best Player Prediction Using Python

This Project can mainly be divided into 3 steps: 1) Scraping the player data from howstat.com using UiPath tool; 2) Predicting the best player based on their stats using Machine Learning Models; 3) Visualizing the Plots using Tkinter GUI.

1) Scraping the player data: Scraping is done using UiPath tool. The main.xaml file consists of all the steps for achieving the same. The PS3 Project.mp4 file is a video showing the working of UiPath tool in scraping and storing the data in an Excel file. The Batsmen.csv and the Bowlers.csv files present inside their respective folders are the outcomes of Step-1.

2) Predicting Players Using Machine Learning: Next, I have used K-Means Clustering technique and Elbow Method to plot all the players based on their total runs scored since 2018 and their respective averages. K-Means Clustering is used for plotting Whereas Elbow Method is used to find the total number of clusters. I have briefed about Elbow Method and K-Means Clustering here: https://documentcloud.adobe.com/link/track?uri=urn%3Aaaid%3Ascds%3AUS%3Aa9af8a27-c908-45e9-a879-c63ca46dbc39 

I have used many classification models such as KNN, SVM, Logistic Regression, Naive Bayes, Decision Trees and Random Forests for predicting the match results of the upcoming tournament. India.py consists of all these models. I have also created a confusion matrix for finding out the performance of these models and Decision Trees turns out to fit my data better compared to the rest of them. It's predicting the outcomes of a match with an accuracy of 63.8%.

3) Visualizing the Plots: For Visualizing the plots Tkinter GUI is selected as it is quite easy to learn and implement. I have visualized the scraped data using bar graphs, pie charts etc. The Tkinter root window consists of a Canvas in the center where all the plotting is done. I have also used another window to display an image along with the name of the player.

Note: Plots can also be visualized without the use of Tkinter. The files which visualizes the same without Tkinter are Batsmen_Prediction.py, Bowlers_Prediction.py and India_Prediction.py. Tkinter is only used as a front-end GUI for the plots.

This is a project which is done for my B-Tech Final Year.
