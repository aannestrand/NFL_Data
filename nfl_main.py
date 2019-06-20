import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,KFold,StratifiedKFold
from sklearn import svm
from sklearn.ensemble import RandomForestRegressor

def __main__():
        df = pd.read_csv('Please.csv')
        X_train, X_test, y_train, y_test = train_test_split(df.drop(['Fantasy Points'],axis=1), df['Fantasy Points'], test_size=.2)

        model = RandomForestRegressor(n_estimators=1000, criterion='mse', max_depth=5, min_samples_split=3, min_samples_leaf=1,
                                     min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None, min_impurity_decrease=0.0,
                                     min_impurity_split=None, bootstrap=True, oob_score=False, n_jobs=None, random_state=None, verbose=0, 
                                     warm_start=False)


        model.fit(X_train, y_train)
        print(model.score(X_test, y_test))

        

__main__()



#This is for making clean csv's
""" def __main__():
    #player_df = pd.read_csv('AFC_Fanduel.csv')
    #print(dfs.getLineups(player_df))

    dfrb = pd.read_csv('2018_RB_W2W.csv')
    dfraw = dfrb.drop(['Pos','Date','Lg','Tm','Unnamed: 8','Opp','Result','Week','Day','Ctch%'],axis=1)
    cols = ['Rush Att/G','Rush Yds/G','Rush TDs/G','Tgt/G','Rec/G','Rec Yds/G']
    zero_data = np.zeros(shape = (len(cols),len(cols)))
    dfavg = pd.DataFrame(columns=cols, data=zero_data)
    dfraw = pd.concat([dfraw,dfavg],axis=1,ignore_index=False)
    dfraw.fillna(value=0, inplace=True)

    for index, row in dfraw.iterrows():
        if (row['G#'] > 1):
                dfplayer = dfraw[dfraw['Player'] == row['Player']]
                dfplayer = dfplayer[dfplayer['G#'] < row['G#']]
                dfraw.at[index,'Rush Yds/G'] = (dfplayer['Rush Yds'].sum())/(row['G#']-1)
                dfraw.at[index,'Rec Yds/G'] = (dfplayer['Rec Yds'].sum())/(row['G#']-1)
                dfraw.at[index,'Rush TDs/G'] = (dfplayer['Rush TDs'].sum())/(row['G#']-1)
                dfraw.at[index,'Rec TDs/G'] = (dfplayer['Rec TDs'].sum())/(row['G#']-1)
                dfraw.at[index,'Rec/G'] = (dfplayer['Rec'].sum())/(row['G#']-1)
                dfraw.at[index,'Tgt/G'] = (dfplayer['Tgt'].sum())/(row['G#']-1)
                dfraw.at[index,'Rush Att/G'] = (dfplayer['Rush Att'].sum())/(row['G#']-1)
                
    dfraw = dfraw[dfraw['G#'] > 1]
    dfraw.drop(['Unnamed: 0','Rush Att','Rush Yds','Rush TDs','Rush Y/A','Tgt','Rec','Rec Yds','Y/Rec','Y/Tgt','Rec Yds','Rec TDs','Player','G#'], axis=1, inplace=True)
    dfraw.to_csv("Please.csv")
 """