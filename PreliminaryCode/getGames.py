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

now = dt.datetime.now()
months = {"January" : "01", "February" : "02", "September" : "09", "October" : "10", "November" : "11", "December": "12"}

year = str(2019)
yeari = 2019
page = r.get("https://www.pro-football-reference.com/years/"+year+"/games.htm")
soup = bs.BeautifulSoup(page.content, "html.parser")
temp = soup.findAll('table')
games = {}
future_games = {}
teams = {}
currentYearOffsetOff = 1
currentYearOffsetDef = 1
currentYear = 2019
numYears = 11

for i in range(numYears):
    
    year = str(currentYear - i)
    yeari = currentYear - i
    if yeari != currentYear and yeari != currentYear-1:
        currentYearOffsetDef = 0
    if yeari != currentYear:
        currentYearOffsetOff = 0

    print(yeari)

    count = 0
    currentTeam = ""

    #games
    page = r.get("https://www.pro-football-reference.com/years/" + year + "/games.htm")
    soup = bs.BeautifulSoup(page.content, "html.parser")
    temp = soup.findAll('td')
    count = 0
    team1 = ""
    team2 = ""
    team1_is_home = True
    score1 = 0
    score2 = 0
    date = year
    if yeari != currentYear:
        for n in temp:
            if (count > 12 or n.text == "Playoffs"):
                count = 0
                team1 = ""
                team2 = ""
                team1_is_home = True
                score1 = 0
                score2 = 0
                date = year
            if (count == 1):
                dateArray = n.text.split(" ")
                if(dateArray[0] == ""):
                    break
                date += months[dateArray[0]]
                day = int(dateArray[1])
                if(day < 10):
                    date += "0"
                date += dateArray[1] 
            if (count == 3 and len(n.text) > 9):
                team1 = n.text
            if (count == 4):
                team1_is_home = n.text != "@"
            if (count == 5):
                team2 = n.text
            if (count == 7 and n.text != ""):
                score1 = float(n.text)
            if (count == 8 and n.text != ""):
                score2 = float(n.text)
                if team1_is_home:
                    games[team1 + " " + team2 + " " + year] = game(team1, team2, score1, score2, yeari, date)
                    games[team1 + " " + team2 + " " + year].getOdds()
                else:
                    games[team2 + " " + team1 + " " + year] = game(team2, team1, score2, score1, yeari, date)
                    games[team2 + " " + team1 + " " + year].getOdds()
            count += 1

with open('games'+'.csv', 'w', newline='') as csvfile:
    output_writer = csv.writer(csvfile, delimiter=',')
    print(len(games))
    for gameKey in games:
        game = games[gameKey]
        row = [game.year, game.home, game.away, game.homeScore, game.awayScore, game.line, game.overUnder]
        output_writer.writerow(row)

