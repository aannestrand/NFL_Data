import nfl_func as nfl
import seaborn as sns
import matplotlib.pyplot as plt


def __main__():
    #plt.figure(figsize=(20,12))
    #sns.barplot(x = (nfl.team_total_def_yards('2018')).index, y =(nfl.team_total_def_yards('2018')).values)
    print(nfl.team_total_off_scoring('2018'))
    
    
__main__()