import pandas as pd
import numpy as np
from itertools import combinations
import re

max_sal = 60000

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
    
df = pd.read_csv('AFC_Fanduel.csv')
playerList = []
playerNameList = []

for i in range(0, len(df)):
    p = Player(df['Nickname'][i], df['Salary'][i], df['FPPG'][i], df['Team'][i], df['Opponent'][i], df['Injury Indicator'][i], df['Game'][i])
    playerList.append(p)
    playerNameList.append(p.name)

lineups = list(combinations(playerNameList, 5))
print(len(lineups))
goodLineups = []

for i in range (0, len(lineups)):
    salary = 0
    for j in range (0, len(lineups[i])):
        for k in range(0, len(playerList)):
            if (lineups[i][j] == playerList[k].name):
                salary += playerList[k].salary
    if(salary >= 48000 and salary <= 50000):
        goodLineups.append(lineups[i])

print(len(goodLineups))