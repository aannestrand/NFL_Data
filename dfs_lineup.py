import pandas as pd
import numpy as np
from itertools import combinations
import re

max_sal = 60000
min_sal = 58000

#Using later
class Player:
    def __init__(self, name, salary, FPPG, team, opp, injury, location):
        self.name = name
        self.salary = salary
        self.FPPG = FPPG
        self.team = team
        self.opp = opp
        self.injury = injury
        self.location = location
    
    def __str__(self):
        return self.name
                       
# returns list of player objects
def getPlayerList (player_df):
    playerList = [] 
    for i in range(0, len(player_df)):
        p = Player(player_df['Nickname'][i], player_df['Salary'][i], player_df['FPPG'][i], player_df['Team'][i], player_df['Opponent'][i], player_df['Injury Indicator'][i], player_df['Game'][i])
        playerList.append(p)

    return playerList

# returns all good lineups
def getLineups (player_df):
    playerList = getPlayerList(player_df)
    playerNameList = []   
    for i in range(0, len(player_df)):
        playerNameList.append(player_df['Nickname'][i])

    lineups = list(combinations(playerNameList, 5))
    goodLineups = []

    for i in range (0, len(lineups)):
        salary = 0
        for j in range (0, len(lineups[i])):
            for k in range(0, len(playerList)):
                if (lineups[i][j] == playerList[k].name):
                    salary += playerList[k].salary
        if(salary >= min_sal and salary <= max_sal):
            for l in range(0, len(lineups[i])):
                diffLineup = list(lineups[i])
                tempPlayer = diffLineup[l]
                diffLineup[l] = diffLineup[0]
                diffLineup[0] = tempPlayer
                goodLineups.append(diffLineup)

    return goodLineups