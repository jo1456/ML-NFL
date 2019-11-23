import pandas as pd
import numpy as np
import bs4 as bs
import requests as r
from team import team
from game import game
year = str(2018)
page = r.get("https://www.pro-football-reference.com/years/"+year+"/games.htm")
soup = bs.BeautifulSoup(page.content, "html.parser")
temp = soup.findAll('td')

count = 0
games = {}
team1 = ""
team2 = ""
team1_is_home = True
score1 = 0
score2 = 0
for n in temp:
    print(n.text)
    if(count > 12 or n.text == "Playoffs"):
        count = 0
        team1 = ""
        team2 = ""
        team1_is_home = True
        score1 = 0
        score2 = 0
    if(count == 3):
        team1 = n.text + " " + year
    if(count == 4):
        team1_is_home = n.text != "@"
    if(count == 5):
        team2 = n.text + " " + year
    if(count == 7 and n.text != ""):
        score1 = float(n.text)
    if(count == 8 and n.text != ""):
        score2 = float(n.text)
        if team1_is_home:
            games[team1 + " " + team2] = game(team1, team2, score1, score2)
        else:
            games[team2 + " " + team1] = game(team2, team1, score2, score1)
    count += 1