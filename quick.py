import pandas as pd
import re

df = pd.read_csv('2018_Receiving_W2W.csv')

for index, row in df.iterrows():
    lol = row['Player'].split("\\")[0]
    df.at[index, 'Player'] = lol

df.to_csv('2018_Receiving_W2W1.csv')