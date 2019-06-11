import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('NFL Play by Play 2009-2018 (v5).csv')

#find team total rushing yards
def team_off_rush_yards(Season):
    #get correct season
    df_season = df[(df['game_date'].apply(lambda date: date.split('-')[0]) == Season)]
    df_season = df_season[df_season['play_type'] == 'run']
    df_season = df_season.groupby('posteam').sum()
    df_rush_season = df_season['yards_gained'].sort_values()
    return(df_rush_season)

#find team total passing yards  
def team_off_pass_yards(Season):
    #get correct season
    df_season = df[(df['game_date'].apply(lambda date: date.split('-')[0]) == Season)]
    df_season = df_season[df_season['play_type'] == 'pass']
    df_season = df_season.groupby('posteam').sum()
    df_pass_season = df_season['yards_gained'].sort_values()
    return(df_pass_season)
 
#find team total offensive yards
def team_total_off_yards(Season):
    #get correct season
    df_season = df[(df['game_date'].apply(lambda date: date.split('-')[0]) == Season)]
    df_season = df_season.groupby('posteam').sum()
    df_yards_season = df_season['yards_gained'].sort_values()
    return(df_yards_season)
 
#find team defensive rush yards
def team_def_rush_yards(Season):
    #get correct season
    df_season = df[(df['game_date'].apply(lambda date: date.split('-')[0]) == Season)]
    df_season = df_season[df_season['play_type'] == 'run']
    df_season = df_season.groupby('defteam').sum()
    df_rush_season = df_season['yards_gained'].sort_values()
    return(df_rush_season)

#find team defensive pass yards    
def team_def_pass_yards(Season):
    #get correct season
    df_season = df[(df['game_date'].apply(lambda date: date.split('-')[0]) == Season)]
    df_season = df_season[df_season['play_type'] == 'pass']
    df_season = df_season.groupby('defteam').sum()
    df_pass_season = df_season['yards_gained'].sort_values()
    return(df_pass_season)
    
#find team total defensive yards
def team_total_def_yards(Season):
    #get correct season
    df_season = df[(df['game_date'].apply(lambda date: date.split('-')[0]) == Season)]
    df_season = df_season.groupby('defteam').sum()
    df_yards_season = df_season['yards_gained'].sort_values()
    return(df_yards_season)
    


    

#ax = plt.figure(figsize=(20,12))
#yo = sns.barplot(x = (team_total_def_yards('2018')).index, y =(team_total_def_yards('2018')).values)
#yo.figure.savefig('total_team_yards_2018.png')