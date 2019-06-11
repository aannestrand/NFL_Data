import pandas as pd
import numpy as np

df1 = pd.read_csv('2018_Rushing_W2W.csv')
df2 = pd.read_csv('2018_Receiving_W2W.csv')

cols = ['Rush Att', 'Rush Yds', 'Rush Y/A', 'Rush TDs']
zero_data = np.zeros(shape=(len(cols),len(cols)))
lol = pd.DataFrame(columns=cols, data=zero_data)
df2 = pd.concat([df2,lol], axis=1)
df2 = df2.fillna(0)
df2.drop(['Unnamed: 0'], axis=1,inplace=True)


for index1, row1 in df1.iterrows():
    for index2, row2 in df2.iterrows():
        if(row1['Player'] == row2['Player'] and row1['G#'] == row2['G#']):
            df2.at[index2, 'Rush Att'] = df1.at[index1, 'Rush Att']
            df2.at[index2, 'Rush Yds'] = df1.at[index1, 'Rush Yds']
            df2.at[index2, 'Rush TDs'] = df1.at[index1, 'Rush TDs']
            df2.at[index2, 'Rush Y/A'] = df1.at[index1, 'Rush Y/A']

df2['Fantasy Points'] = (df2['Rush Yds']+df2['Rec Yds'])*.1+(df2['Rush TDs']+df2['Rec TDs'])*6+(df2['Rec']*.5)
df2.to_csv('Test1.csv')
