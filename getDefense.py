year = str(2018 - i)
    page = r.get("https://www.pro-football-reference.com/years/" + year + "/opp.htm")
    soup = bs.BeautifulSoup(page.content, "html.parser")
    temp = soup.findAll('div',attrs={"class":"table_wrapper"})

    count = 0
    currentTeam = ""

    numberOfDrives = 0
    plays = 0
    scorePercent = 0
    toPercent = 0
    playsPerDrive = 0
    yardsPerDrive = 0
    start = 0
    time = 0
    ptsPerDrive = 0
    thirdPct = 0.0
    fourthAttempts = 0.0
    fourthConversions = 0.0
    fourthPct = 0.0
    rdAttemtps = 0
    rdTds = 0
    rdPct = 0.0
    fgPct = 0.0
    xpPct = 0.0
    yardsPerPunt = 0.0
    puntYards = 0.0
    kickYards = 0.0
    completed = 0.0
    attempted = 0.0
    compPct = 0.0
    yards = 0.0
    tdPct = 0.0
    ints = 0.0
    intPct = 0.0
    yardsPerAttempt = 0.0
    adjustedYardsPerAttempt = 0.0
    yardsPerCatch = 0.0
    yardsPerGame = 0.0
    qbr = 0.0
    sacks = 0.0
    yardsLostDueToSacks = 0.0
    netYardsPerPassAttempt = 0.0
    adjustedNetYardsPerPassAttempt = 0.0
    sackRate = 0.0
    comebacks = 0.0
    gameWinningDrives = 0.0
    pointsFromPassing = 0.0
    attempts = 0.0
    tds = 0
    yardsPerCarry = 0.0
    yardsPerGame = 0.0
    fumbles = 0.0
    pointsFromRush = 0.0


    table = str(list(temp)[7]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    #driveAvgs
    for n in list(temp2):
        currText = n.text
        if(count >= 11):
            count = 0
            teams[currentTeam].setDriveAvgs(driveAvgs(numberOfDrives, plays, scorePercent, toPercent, playsPerDrive, yardsPerDrive, start, time, ptsPerDrive))
        if count  == 0:
            numberOfDrives = 0
            plays = 0
            scorePercent = 0
            toPercent = 0
            playsPerDrive = 0
            yardsPerDrive = 0
            start = 0
            time = 0
            ptsPerDrive = 0
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
            currentTeam = currText + " " + str(year)
            teams[currentTeam] = team()
            teams[currentTeam].name = currentTeam
        elif count == 2:
            numberOfDrives = float(currText)
        elif (count == 3):
            plays = float(currText)
        elif (count == 4):
            scorePercent = float(currText)
        elif (count == 5):
            toPercent = float(currText)
        elif (count == 6):
            playsPerDrive = float(currText)
        elif (count == 7):
            yardsPerDrive = float(currText)
        elif (count == 8):
            start = float(currText.replace("Own", ""))
        elif (count == 9):
            time = float(currText.split(':')[0]) + float(currText.split(':')[1])/60.0
        elif (count == 10):
            ptsPerDrive = float(currText)
        count += 1

    #conversions
    table = str(list(temp)[6]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    count = 0
    for n in list(temp2):
        currText = n.text
        if(count >= 11):
            count = 0
            teams[currentTeam].setConversionsAgainst(conversions(thirdPct, fourthAttempts, fourthConversions, fourthPct, rdAttemtps, rdTds, rdPct))
            thirdPct = 0.0
            fourthAttempts = 0.0
            fourthConversions = 0.0
            fourthPct = 0.0
            rdAttemtps = 0
            rdTds = 0
            rdPct = 0.0
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
        if count == 0:
            currentTeam = currText + " " + str(year)
        elif count == 4:
            thirdPct = float(currText)
        elif (count == 5):
            fourthAttempts = float(currText)
        elif (count == 6):
            fourthConversions = float(currText)
        elif (count == 7):
            fourthPct = float(currText)
        elif (count == 8):
            rdAttemtps = float(currText)
        elif (count == 9):
            rdTds = float(currText)
        elif (count == 10):
            rdPct = float(currText)
        count += 1

    #kicking
    table = str(list(temp)[4]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    count = 0
    for n in list(temp2):
        currText = n.text
        if(count > 12):
            count = 0
            teams[currentTeam].setKickingAgainst(kicking(fgPct, xpPct, yardsPerPunt))
            fgPct = 0.0
            xpPct = 0.0
            yardsPerPunt = 0.0
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
        if count == 0:
            currentTeam = currText + " " + str(year)
        elif count == 4:
            fgPct = float(currText)
        elif (count == 7):
            xpPct = float(currText)
        elif (count == 11):
            yardsPerPunt = float(currText)
        count += 1

    #returns
    table = str(list(temp)[3]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    count = 0
    for n in list(temp2):
        currText = n.text
        if(count >= 10):
            count = 0
            teams[currentTeam].setKickReturnsAgainst(kickReturns(puntYards, kickYards))
            puntYards = 0.0
            kickYards = 0.0
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
        if count == 0:
            currentTeam = currText + " " + str(year)
        elif count == 5:
            puntYards = float(currText)
        elif (count == 9):
            kickYards = float(currText)
        count += 1

    #rushing
    table = str(list(temp)[2]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    count = 0
    for n in list(temp2):
        currText = n.text
        if(count >= 8):
            count = 0
            teams[currentTeam].setRushingOffAgainst(rushingOff(attempts, yards, tds, yardsPerCarry, yardsPerGame, fumbles, pointsFromRush))
            attempts = 0
            yards = 0.0
            tds = 0
            yardsPerCarry = 0.0
            yardsPerGame = 0.0
            fumbles = 0
            pointsFromRush = 0.0
            if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
                break
        if count == 0:
            currentTeam = currText + " " + str(year)
        elif count == 2:
            attempts = float(currText)
        elif (count == 3):
            yards = float(currText)
        elif (count == 4):
            tds = float(currText)
        elif (count == 6):
            yardsPerCarry = float(currText)
        elif (count == 7):
            yardsPerGame = float(currText)
        count += 1

    #passing defense
    table = str(list(temp)[1]).replace("<!--", "").replace("-->", "").replace("%", "")
    soup2 = bs.BeautifulSoup(table, "html.parser")
    temp2 = soup2.find_all('td')
    count = 0
    for n in list(temp2):
        currText = n.text
        if currText == "":
            currText = "0"
        if(count >= 18):
            count = 0
            teams[currentTeam].setPassingDefense(defense(attempted, aompleted, compPct, yds, td, dadot, air, yac, blitz, blitzPct, hurry, hurryPct,
                qbkd, qbkdPct, sacks, pressure, pressurePct, missedTackles))
        attempted = 0
        completed = 0
        yds = 0.0
        td = 0
        dadot = 0.0
        air = 0.0
        yac = 0.0
        blitz = 0
        blitzPct = 0.0
        hurry = 0.0
        hurryPct = 0.0
        qbkd = 0.0
        qbkdPct = 0.0
        sacks = 0.0
        pressure = 0.0
        pressurePct = 0.0
        missedTackles = 0.0
        if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
            break
        if count == 0:
            currentTeam = currText + " " + str(year)
        elif count == 3:
            completed = float(currText)
        elif count == 2:
            attempted = float(currText)
        elif count == 4:
            yards = float(currText)
        elif count == 5:
            td = float(currText)
        elif count == 6:
            dadot = float(currText)
        elif count == 7:
            air = float(currText)
        elif count == 8:
            yac = float(currText)
        elif count == 9:
            blitz = float(currText)
        elif count == 10:
            blitzPct = float(currText)
        elif count == 11:
            hurry = float(currText)
        elif count == 12:
            hurryPct = float(currText)
        elif count == 13:
            qbkd = float(currText)
        elif count == 14:
            qbkdPct = float(currText)
        elif count == 15:
            sacks = float(currText)
        elif count == 16:
            pressure = float(currText)
        elif count == 17:
            pressurePct = float(currText)
        elif count == 18:
            missedTackles = float(currText)
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
        if(count >= 26):
            count = 0
            teams[currentTeam].setGeneralDefense(generalDefense(fumbles, ints, penaltyYards, penaltyFirstDowns))
        fumbles = 0
        ints = 0
        penaltyYards = 0.0
        penaltyFirstDowns = 0
        if (currText == "League Total" or currText == "Avg Team" or currText == "Avg Tm/G"):
            break
        if count == 0:
            currentTeam = currText + " " + str(year)
        elif count == 7:
            fumbles = float(currText)
        elif count == 13:
            ints = float(currText)
        elif count == 22:
            penaltyYards = float(currText)
        elif count == 23:
            penaltyFirstDowns = float(currText)
        count += 1