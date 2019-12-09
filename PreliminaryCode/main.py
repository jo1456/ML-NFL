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

    page = r.get("https://www.pro-football-reference.com/years/"+year+"/#all_team_stats")
    soup = bs.BeautifulSoup(page.content, "html.parser")
    temp = soup.findAll('div',attrs={"class":"table_wrapper"})

    count = 0
    currentTeam = ""

    #conversions
    table = str(list(temp)[11-currentYearOffsetOff]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    count = 0
    for n in list(temp2):
        currText = n.text
        if(count == 11):
            count = 0
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
        if count == 0:
            currentTeam = currText + " " + str(year)
            teams[currentTeam] = team()
            teams[currentTeam].name = currText
            teams[currentTeam].setConversions(conversions(0, 0, 0, 0, 0, 0, 0))
        elif count == 4:
            teams[currentTeam].Conversions.thirdPct = float(currText)
        elif (count == 5):
            teams[currentTeam].Conversions.fourthAttempts = float(currText)
        elif (count == 6):
            teams[currentTeam].Conversions.fourthConversions = float(currText)
        elif (count == 7):
            teams[currentTeam].Conversions.fourthPct = float(currText)
        elif (count == 8):
            teams[currentTeam].Conversions.rdAttemtps = float(currText)
        elif (count == 9):
            teams[currentTeam].Conversions.rdTds = float(currText)
        elif (count == 10):
            teams[currentTeam].Conversions.rdPct = float(currText)
        count += 1

    table = str(list(temp)[12-currentYearOffsetOff]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    #driveAvgs
    for n in list(temp2):
        currText = n.text
        if(count == 11):
            count = 0
        if count  == 0:
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
            currentTeam = currText + " " + str(year)
            teams[currentTeam].setDriveAvgs(driveAvgs(0, 0, 0, 0, 0, 0, 0, 0, 0))
        elif count == 2:
            teams[currentTeam].DriveAvgs.numberOfDrives = float(currText)
        elif (count == 3):
            teams[currentTeam].DriveAvgs.plays = float(currText)
        elif (count == 4):
            teams[currentTeam].DriveAvgs.scorePercent = float(currText)
        elif (count == 5):
            teams[currentTeam].DriveAvgs.toPercent = float(currText)
        elif (count == 6):
            teams[currentTeam].DriveAvgs.playsPerDrive = float(currText)
        elif (count == 7):
            teams[currentTeam].DriveAvgs.yardsPerDrive = float(currText)
        elif (count == 8):
            teams[currentTeam].DriveAvgs.start = float(currText.replace("Own", ""))
        elif (count == 9):
            teams[currentTeam].DriveAvgs.time = float(currText.split(':')[0]) + float(currText.split(':')[1])/60.0
        elif (count == 10):
            teams[currentTeam].DriveAvgs.ptsPerDrive = float(currText)
        count += 1

    #kicking
    table = str(list(temp)[9-currentYearOffsetOff]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    count = 0
    for n in list(temp2):
        currText = n.text
        if(count > 23):
            count = 0
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
        if count == 0:
            currentTeam = currText + " " + str(year)
            teams[currentTeam].setKicking(kicking(0,0,0))
        elif count == 14:
            teams[currentTeam].Kicking.fgPct = float(currText)
        elif (count == 17):
            teams[currentTeam].Kicking.xpPct = float(currText)
        elif (count == 22):
            teams[currentTeam].Kicking.yardsPerPunt = float(currText)
        count += 1

    #returns
    table = str(list(temp)[8-currentYearOffsetOff]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    count = 0
    for n in list(temp2):
        currText = n.text
        if(count == 13):
            count = 0
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
        if count == 0:
            currentTeam = currText + " " + str(year)
            teams[currentTeam].setKickReturns(kickReturns(0,0))
        elif count == 6:
            teams[currentTeam].KickReturns.puntYards = float(currText)
        elif (count == 11):
            teams[currentTeam].KickReturns.kickYards = float(currText)
        count += 1

    #rushing
    table = str(list(temp)[7-currentYearOffsetOff]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    count = 0
    for n in list(temp2):
        currText = n.text
        if(count == 10):
            count = 0
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
        if count == 0:
            currentTeam = currText + " " + str(year)
            teams[currentTeam].setRushingOff(rushingOff(0, 0, 0, 0, 0, 0, 0))
        elif count == 2:
            teams[currentTeam].RushingOff.attempts = float(currText)
        elif (count == 3):
            teams[currentTeam].RushingOff.yards = float(currText)
        elif (count == 4):
            teams[currentTeam].RushingOff.tds = float(currText)
        elif (count == 6):
            teams[currentTeam].RushingOff.yardsPerCarry = float(currText)
        elif (count == 7):
            teams[currentTeam].RushingOff.yardsPerGame = float(currText)
        elif (count == 8):
            teams[currentTeam].RushingOff.fumbles = float(currText)
        elif (count == 9):
            teams[currentTeam].RushingOff.pointsFromRush = float(currText)
        count += 1

    #passing
    table = str(list(temp)[6-currentYearOffsetOff]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    count = 0
    for n in list(temp2):
        currText = n.text
        if currText == "":
            currText = "0"
        if(count == 24):
            count = 0
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
        if count == 0:
            currentTeam = currText + " " + str(year)
            teams[currentTeam].setPassingOff(passingOff(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
        elif count == 2:
            teams[currentTeam].PassingOff.completed = float(currText)
        elif count == 3:
            teams[currentTeam].PassingOff.attempted = float(currText)
        elif count == 4:
            teams[currentTeam].PassingOff.compPct = float(currText)
        elif count == 5:
            teams[currentTeam].PassingOff.yards = float(currText)
        elif count == 6:
            teams[currentTeam].PassingOff.td = float(currText)
        elif count == 7:
            teams[currentTeam].PassingOff.tdPct = float(currText)
        elif count == 8:
            teams[currentTeam].PassingOff.int = float(currText)
        elif count == 9:
            teams[currentTeam].PassingOff.intPct = float(currText)
        elif count == 11:
            teams[currentTeam].PassingOff.yardsPerAttempt = float(currText)
        elif count == 14:
            teams[currentTeam].PassingOff.yardsPerGame = float(currText)
        elif count == 15:
            teams[currentTeam].PassingOff.qbr = float(currText)
        elif count == 16:
            teams[currentTeam].PassingOff.sacks = float(currText)
        elif count == 17:
            teams[currentTeam].PassingOff.yardsLostDueToSacks = float(currText)
        elif count == 18:
            teams[currentTeam].PassingOff.netYardsPerPassAttempt = float(currText)
        elif count == 19:
            teams[currentTeam].PassingOff.adjustedNetYardsPerPassAttempt = float(currText)
        elif count == 20:
            teams[currentTeam].PassingOff.sackRate = float(currText)
        elif count == 21:
            teams[currentTeam].PassingOff.comebacks = float(currText)
        elif count == 22:
            teams[currentTeam].PassingOff.gameWinningDrives = float(currText)
        elif count == 23:
            teams[currentTeam].PassingOff.pointsFromPassing = float(currText)
        count += 1

    #off penalties
    table = str(list(temp)[5-currentYearOffsetOff]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    count = 0
    for n in list(temp2):
        currText = n.text
        if currText == "":
            currText = "0"
        if(count >= 27):
            count = 0
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
        if count == 0:
            currentTeam = currText + " " + str(year)
            teams[currentTeam].setOffensePenalties(offensePenalties(0,0))
        elif count == 22:
            teams[currentTeam].OffensePenalties.yards = float(currText)
        elif count == 23:
            teams[currentTeam].OffensePenalties.penaltyFirstDowns = float(currText)
        count += 1

    #defense
    page = r.get("https://www.pro-football-reference.com/years/" + year + "/opp.htm")
    soup = bs.BeautifulSoup(page.content, "html.parser")
    temp = soup.findAll('div',attrs={"class":"table_wrapper"})

    count = 0
    currentTeam = ""

    currentYearOffset = 1
    if(yeari != currentYear or yeari != currentYear - 1):
        currentYearOffset = 0

    table = str(list(temp)[7+currentYearOffsetDef]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    #driveAvgs
    for n in list(temp2):
        currText = n.text
        if(count >= 11):
            count = 0
        if count  == 0:
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
            currentTeam = currText + " " + str(year)
            teams[currentTeam].setDriveAvgsAgainst(driveAvgs(0,0,0,0,0,0,0,0,0))
        elif count == 2:
            teams[currentTeam].DriveAvgsAgainst.numberOfDrives = float(currText)
        elif (count == 3):
            teams[currentTeam].DriveAvgsAgainst.plays = float(currText)
        elif (count == 4):
            teams[currentTeam].DriveAvgsAgainst.scorePercent = float(currText)
        elif (count == 5):
            teams[currentTeam].DriveAvgsAgainst.toPercent = float(currText)
        elif (count == 6):
            teams[currentTeam].DriveAvgsAgainst.playsPerDrive = float(currText)
        elif (count == 7):
            teams[currentTeam].DriveAvgsAgainst.yardsPerDrive = float(currText)
        elif (count == 8):
            teams[currentTeam].DriveAvgsAgainst.start = float(currText.replace("Own", ""))
        elif (count == 9):
            teams[currentTeam].DriveAvgsAgainst.time = float(currText.split(':')[0]) + float(currText.split(':')[1])/60.0
        elif (count == 10):
            teams[currentTeam].DriveAvgsAgainst.ptsPerDrive = float(currText)
        count += 1

    #conversions
    table = str(list(temp)[6+currentYearOffsetDef]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    count = 0
    for n in list(temp2):
        currText = n.text
        if(count >= 11):
            count = 0
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
        if count == 0:
            currentTeam = currText + " " + str(year)
            teams[currentTeam].setConversionsAgainst(conversions(0,0,0,0,0,0,0))
        elif count == 4:
            teams[currentTeam].ConversionsAgainst.thirdPct = float(currText)
        elif (count == 5):
            teams[currentTeam].ConversionsAgainst.fourthAttempts = float(currText)
        elif (count == 6):
            teams[currentTeam].ConversionsAgainst.fourthConversions = float(currText)
        elif (count == 7):
            teams[currentTeam].ConversionsAgainst.fourthPct = float(currText)
        elif (count == 8):
            teams[currentTeam].ConversionsAgainst.rdAttemtps = float(currText)
        elif (count == 9):
            teams[currentTeam].ConversionsAgainst.rdTds = float(currText)
        elif (count == 10):
            teams[currentTeam].ConversionsAgainst.rdPct = float(currText)
        count += 1

    #kicking
    table = str(list(temp)[4+currentYearOffsetDef]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    count = 0
    for n in list(temp2):
        currText = n.text
        if(count >= 12):
            count = 0
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
        if count == 0:
            currentTeam = currText + " " + str(year)
            teams[currentTeam].setKickingAgainst(kicking(0,0,0))
        elif count == 4:
            teams[currentTeam].KickingAgainst.fgPct = float(currText)
        elif (count == 7):
            teams[currentTeam].KickingAgainst.xpPct = float(currText)
        elif (count == 11):
            teams[currentTeam].KickingAgainst.yardsPerPunt = float(currText)
        count += 1

    #returns
    table = str(list(temp)[3+currentYearOffsetDef]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    count = 0
    for n in list(temp2):
        currText = n.text
        if(count >= 10):
            count = 0
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
        if count == 0:
            currentTeam = currText + " " + str(year)
            teams[currentTeam].setKickReturnsAgainst(kickReturns(0,0))
        elif count == 5:
            teams[currentTeam].KickReturnsAgainst.puntYards = float(currText)
        elif (count == 9):
            teams[currentTeam].KickReturnsAgainst.kickYards = float(currText)
        count += 1

    #rushing
    table = str(list(temp)[2+currentYearOffsetDef]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    count = 0
    for n in list(temp2):
        currText = n.text
        if(count >= 8):
            count = 0
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
        if count == 0:
            currentTeam = currText + " " + str(year)
            teams[currentTeam].setRushingOffAgainst(rushingOff(0,0,0,0,0,0,0))
        elif count == 2:
            teams[currentTeam].RushingOffAgainst.attempts = float(currText)
        elif (count == 3):
            teams[currentTeam].RushingOffAgainst.yards = float(currText)
        elif (count == 4):
            teams[currentTeam].RushingOffAgainst.tds = float(currText)
        elif (count == 6):
            teams[currentTeam].RushingOffAgainst.yardsPerCarry = float(currText)
        elif (count == 7):
            teams[currentTeam].RushingOffAgainst.yardsPerGame = float(currText)
        count += 1

    #passing defense
    table = str(list(temp)[1+currentYearOffsetDef]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    count = 0
    for n in list(temp2):
        currText = n.text
        if currText == "":
            currText = "0"
        if(count >= 24):
            count = 0
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
        if count == 0:
            currentTeam = currText + " " + str(year)
            teams[currentTeam].setPassingDefense(passingOff(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
        elif count == 2:
            teams[currentTeam].PassingDefense.completed = float(currText)
        elif count == 3:
            teams[currentTeam].PassingDefense.attempted = float(currText)
        elif count == 4:
            teams[currentTeam].PassingDefense.compPct = float(currText)
        elif count == 5:
            teams[currentTeam].PassingDefense.yards = float(currText)
        elif count == 6:
            teams[currentTeam].PassingDefense.td = float(currText)
        elif count == 7:
            teams[currentTeam].PassingDefense.tdPct = float(currText)
        elif count == 8:
            teams[currentTeam].PassingDefense.ints = float(currText)
        elif count == 10:
            teams[currentTeam].PassingDefense.intPct = float(currText)
        elif count == 11:
            teams[currentTeam].PassingDefense.yardsPerAttempt = float(currText)
        elif count == 14:
            teams[currentTeam].PassingDefense.yardsPerGame = float(currText)
        elif count == 15:
            teams[currentTeam].PassingDefense.qbr = float(currText)
        elif count == 16:
            teams[currentTeam].PassingDefense.sacks = float(currText)
        elif count == 17:
            teams[currentTeam].PassingDefense.yardsLostDueToSacks = float(currText)
        elif count == 20:
            teams[currentTeam].PassingDefense.netYardsPerPassAttempt = float(currText)
        elif count == 21:
            teams[currentTeam].PassingDefense.adjustedNetYardsPerPassAttempt = float(currText)
        elif count == 22:
            teams[currentTeam].PassingDefense.sackRate = float(currText)
        elif count == 23:
            teams[currentTeam].PassingDefense.pointsFromPassing = float(currText)
        count += 1    

    #general defense
    table = str(list(temp)[0]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    count = 0
    for n in list(temp2):
        currText = n.text
        if currText == "":
            currText = "0"
        if(count >= 27):
            count = 0
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
        if count == 0:
            currentTeam = currText + " " + str(year)
            teams[currentTeam].setGeneralDefense(generalDefense(0,0,0,0))
        elif count == 7:
            teams[currentTeam].GeneralDefense.fumbles = float(currText)
        elif count == 13:
            teams[currentTeam].GeneralDefense.ints = float(currText)
        elif count == 22:
            teams[currentTeam].GeneralDefense.penaltyYards = float(currText)
        elif count == 23:
            teams[currentTeam].GeneralDefense.penaltyFirstDowns = float(currText)
        count += 1
    
#games    
with open("games.csv") as gamesCsv:
    line = gamesCsv.readline()
    gameArray = line.split("\\n")[0].split(",")
    while line:
        tempGame = game(gameArray[1], gameArray[2], gameArray[3], gameArray[4], gameArray[0], "")
        tempGame.spread = float(gameArray[5])
        tempGame.overUnder = float(gameArray[6])
        games[gameArray[1] + " " + gameArray[0] + " " + gameArray[2] + " " + gameArray[0]] = tempGame
        line = gamesCsv.readline()
        gameArray = line.split("\\n")[0].split(",")

#upcoming games
#https://www.pro-football-reference.com/years/2019/games.htm
page = r.get("https://www.pro-football-reference.com/years/" + "2019" + "/games.htm")
soup = bs.BeautifulSoup(page.content, "html.parser")
temp = soup.findAll('td')
count = 0
team1 = ""
team2 = ""
team1_is_home = True
score1 = 0
score2 = 0
month = 0
day = 0
week = 0
currentWeek = 0
year = "2019"
yeari = 2019
date = year
for n in temp:
    if (count > 12 or n.text == "Playoffs"):
        count = 0
        team1 = ""
        team2 = ""
        team1_is_home = True
        score1 = 0
        score2 = 0
        month = 0
        day = 0
        date = year
    if(count == 0 and n.text == "Thu"):
        currentWeek += 1
    if(count == 1):
        dateArray = n.text.split(" ")
        month = int(months[dateArray[0]])
        day = int(dateArray[1])
    if (count == 3 and len(n.text) > 9):
        team1 = n.text
    if (count == 4):
        team1_is_home = n.text != "@"
    if (count == 5):
        team2 = n.text
    if (count == 8):
        if(month > now.month or (day >= now.day and month == now.month)):
            if(week == 0):
                week = currentWeek
            if(week == currentWeek):
                if team1_is_home:
                    future_games[team1 + " " + team2] = game(team1, team2, score1, score2, yeari, date)
                else:
                    future_games[team2 + " " + team1] = game(team2, team1, score2, score1, yeari, date)
    count += 1

with open('train'+'.csv', 'w', newline='') as csvfile:
    output_writer = csv.writer(csvfile, delimiter=',')
    for gameKey in games:
        game = games[gameKey]
        team = game.home+" "+str(game.year)
        print(team)
        if team in teams and int(game.year) != yeari:
            
            home = teams[game.home+ " " +str(game.year)]
            away = teams[game.away+ " " +str(game.year)]

            #home
            passYardsAndRedZone = (home.PassingOff.yardsPerGame + away.PassingDefense.yardsPerGame)*(home.Conversions.rdPct + away.ConversionsAgainst.rdPct)/4
            rushYardsAndRedZone = (home.RushingOff.yardsPerGame + away.RushingOffAgainst.yardsPerGame)*(home.Conversions.rdPct + away.ConversionsAgainst.rdPct)/4 
            turnovers = ((home.DriveAvgs.toPercent + away.DriveAvgsAgainst.toPercent) / 2)
            penalties = (away.GeneralDefense.penaltyYards - home.OffensePenalties.penaltyYards)
            sacks = (home.PassingOff.sacks + away.PassingDefense.sacks) / 2
            startingPosition = (home.DriveAvgs.start + away.DriveAvgsAgainst.start)/2
            pointsPerDrive = (home.DriveAvgs.ptsPerDrive + away.DriveAvgsAgainst.ptsPerDrive)/2
            thirdPct = (home.Conversions.thirdPct + away.ConversionsAgainst.thirdPct)/2
            completionPct = (home.PassingOff.compPct + away.PassingDefense.compPct)/2
            row = [game.year, game.home, passYardsAndRedZone, rushYardsAndRedZone, turnovers, penalties, sacks, startingPosition, pointsPerDrive, thirdPct, completionPct, 1, game.homeScore]
            output_writer.writerow(row)

            #away
            passYardsAndRedZone = (away.PassingOff.yardsPerGame + home.PassingDefense.yardsPerGame)*(away.Conversions.rdPct + home.ConversionsAgainst.rdPct)/4
            rushYardsAndRedZone = (away.RushingOff.yardsPerGame + home.RushingOffAgainst.yardsPerGame)*(away.Conversions.rdPct + home.ConversionsAgainst.rdPct)/4
            turnovers = ((away.DriveAvgs.toPercent + home.DriveAvgsAgainst.toPercent) / 2)
            penalties = (home.GeneralDefense.penaltyYards - away.OffensePenalties.penaltyYards) 
            sacks = (away.PassingOff.sacks + home.PassingDefense.sacks) / 2
            startingPosition = (away.DriveAvgs.start + home.DriveAvgsAgainst.start)/2
            pointsPerDrive = (away.DriveAvgs.ptsPerDrive + home.DriveAvgsAgainst.ptsPerDrive)/2
            thirdPct = (away.Conversions.thirdPct + home.ConversionsAgainst.thirdPct)/2
            completionPct = (away.PassingOff.compPct + home.PassingDefense.compPct)/2
            row = [game.year, game.away, passYardsAndRedZone, rushYardsAndRedZone, turnovers, penalties, sacks, startingPosition, pointsPerDrive, thirdPct, completionPct, 0, game.awayScore]
            output_writer.writerow(row)

with open('test.csv', 'w', newline='') as csvfile:
    output_writer = csv.writer(csvfile, delimiter=',')
    for gameKey in future_games:
        game = future_games[gameKey]
        if game.home in teams:
            
            home = teams[game.home+str(game.year)]
            away = teams[game.away+str(game.year)]

            #if(home.name != "Atlanta Falcons 2019" and away.name != "Atlanta Falcons 2019"):
                #home
            passYardsAndRedZone = (home.PassingOff.yardsPerGame + away.PassingDefense.yardsPerGame)*(home.Conversions.rdPct + away.ConversionsAgainst.rdPct)/4
            rushYardsAndRedZone = (home.RushingOff.yardsPerGame + away.RushingOffAgainst.yardsPerGame)*(home.Conversions.rdPct + away.ConversionsAgainst.rdPct)/4 
            turnovers = ((home.DriveAvgs.toPercent + away.DriveAvgsAgainst.toPercent) / 2)
            penalties = (away.GeneralDefense.penaltyYards - home.OffensePenalties.penaltyYards)
            sacks = (home.PassingOff.sacks + away.PassingDefense.sacks) / 2
            startingPosition = (home.DriveAvgs.start + away.DriveAvgsAgainst.start)/2
            pointsPerDrive = (home.DriveAvgs.ptsPerDrive + away.DriveAvgsAgainst.ptsPerDrive)/2
            thirdPct = (home.Conversions.thirdPct + away.ConversionsAgainst.thirdPct)/2
            completionPct = (home.PassingOff.compPct + away.PassingDefense.compPct)/2
            row = [home.name, passYardsAndRedZone, rushYardsAndRedZone, turnovers, penalties, sacks, startingPosition, pointsPerDrive, thirdPct, completionPct, 1, game.homeScore]
            output_writer.writerow(row)

            #away
            passYardsAndRedZone = (away.PassingOff.yardsPerGame + home.PassingDefense.yardsPerGame)*(away.Conversions.rdPct + home.ConversionsAgainst.rdPct)/4
            rushYardsAndRedZone = (away.RushingOff.yardsPerGame + home.RushingOffAgainst.yardsPerGame)*(away.Conversions.rdPct + home.ConversionsAgainst.rdPct)/4
            turnovers = ((away.DriveAvgs.toPercent + home.DriveAvgsAgainst.toPercent) / 2)
            penalties = (home.GeneralDefense.penaltyYards - away.OffensePenalties.penaltyYards) 
            sacks = (away.PassingOff.sacks + home.PassingDefense.sacks) / 2
            startingPosition = (away.DriveAvgs.start + home.DriveAvgsAgainst.start)/2
            pointsPerDrive = (away.DriveAvgs.ptsPerDrive + home.DriveAvgsAgainst.ptsPerDrive)/2
            thirdPct = (away.Conversions.thirdPct + home.ConversionsAgainst.thirdPct)/2
            completionPct = (away.PassingOff.compPct + home.PassingDefense.compPct)/2
            row = [away.name, passYardsAndRedZone, rushYardsAndRedZone, turnovers, penalties, sacks, startingPosition, pointsPerDrive, thirdPct, completionPct, 0, game.awayScore]
            output_writer.writerow(row)
