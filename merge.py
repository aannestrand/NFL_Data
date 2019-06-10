## Merging out csv's into one big csv

import pandas as pd
import os

main = pd.read_csv("2018_RUSstats_Wk1.csv")
main.drop(['Unnamed: 0','Rk'], axis=1, inplace=True)
print(main)

for i in range(2, 18):
    fileName = "2018_RUSstats_Wk" + str(i) + ".csv"
    df = pd.read_csv(fileName)
    df.drop(['Unnamed: 0','Rk'], axis=1, inplace=True)
    print(df.head())
    main = main.append(df, ignore_index=True)

for i, row in main.iterrows():
    if (row['Player'] == 'Player'):
        main.drop(i, inplace=True)

main.to_csv('2018_Rushing_W2W.csv')