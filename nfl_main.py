import dfs_lineup as dfs
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nfl_team_stats as stats


def __main__():
    #player_df = pd.read_csv('AFC_Fanduel.csv')
    #print(dfs.getLineups(player_df))

    dfrb = pd.read_csv('2018_RB_W2W.csv')
    dfraw = dfrb.drop(['Player','Pos','Date','Lg','Tm','Unnamed: 8','Opp','Result','Week','Day','Ctch%'],axis=1)

    sns.set(style="whitegrid")
    f, ax = plt.subplots(figsize=(6.5, 6.5))
    sns.scatterplot(x='Opp RYPG',y='Fantasy Points',data=dfrb,ax=ax)
    f.show()

__main__()
