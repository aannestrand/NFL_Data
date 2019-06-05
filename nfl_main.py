import dfs_lineup as dfs
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def __main__():
    player_df = pd.read_csv('AFC_Fanduel.csv')
    print(dfs.getLineups(player_df))
    
__main__()