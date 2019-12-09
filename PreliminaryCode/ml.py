import pandas as pd
import numpy as np
import bs4 as bs
import requests as r
import csv
from team import team, create_row
from game import game
from driveAvgs import driveAvgs
from rushingOff import rushingOff
from passingOff import passingOff
from kicking import kicking
from kickReturns import kickReturns
from conversions import conversions
from passingDefense import passingDefense
from generalDefense import generalDefense
from offensePenalties import offensePenalties
import datetime as dt
from sklearn import linear_model, model_selection
from sklearn.preprocessing import PolynomialFeatures
import numpy.polynomial.polynomial as poly

headers = ["Name", "PassYPG", "RushYPG" , "Home", "Score"]
test = pd.read_csv("test.csv", header=None)

oldData = pd.read_csv("train"+".csv", header=None)
length = oldData.shape[1] 
numSamples = oldData.shape[0]
rsq = 0
kf = model_selection.KFold(n_splits=5)
for train, test in kf.split(oldData):

	trainX = oldData.iloc[train,:length-1]
	trainY = oldData.iloc[train,length-1:]
	testX = oldData.iloc[test,:length-1]
	testY = oldData.iloc[test,length-1:]

	regr = linear_model.LinearRegression()
	regr.fit(trainX, trainY)
	pred_y = regr.predict(testX)

	rss = np.mean((pred_y - testY)**2)/(np.std(testY)**2)
	rsq += (1 - (rss))/5

print(rsq)

#testX = test.iloc[:,1:length]
#testTeams = test.iloc[:,0:1]
#for j in range(len(testY)//2):
#	i = j*2
#	print(testTeams.iloc[i][0] + " " + testTeams.iloc[i+1][0] + ":")
#
#	if(round(testY[i][0], 2) > round(testY[i+1][0], 2)):
#		print(testTeams.iloc[i][0] + " by " + str(round((testY[i][0]) - (testY[i+1][0]),2)))
#	else:
#		print(testTeams.iloc[i+1][0] + " by " + str(round((testY[i+1][0]) - (testY[i][0]),2)))
#
#	print("Total: " + str(round((testY[i+1][0]) + (testY[i][0]),2)))
#
#	print("==========")
