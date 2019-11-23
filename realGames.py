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

test = pd.read_csv("test.csv", header=None)
oldData = pd.read_csv("train"+".csv", header=None)

length = oldData.shape[1] 
numSamples = oldData.shape[0]
trainX = oldData.iloc[:,:length-1]
trainY = oldData.iloc[:,length-1:]

regr = linear_model.LinearRegression()
regr.fit(trainX, trainY)

testX = test.iloc[:,1:length]
testY = regr.predict(testX)

testTeams = test.iloc[:,0:1]

for j in range(len(testY)//2):
	i = j*2

	team1 = testTeams.iloc[i][0].split("2019")[0]
	team2 = testTeams.iloc[i+1][0].split("2019")[0]
	team1Score = round((testY[i][0]),2)
	team2Score = round((testY[i+1][0]),2)

	print(team1 + " " + str(team1Score))
	print(team2 + " " + str(team2Score))

	if(team1Score > team2Score):
		print(team1 + " by " + str(round(team1Score - team2Score, 2)))
	else:
		print(team2 + " by " + str(round(team2Score - team1Score, 2)))

	print("Total: " + str(round(team1Score+team2Score,2)))

	print("==========")