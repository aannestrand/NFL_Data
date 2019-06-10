## Use this program to scrap table online for data

import requests
import urllib.request
import time
import lxml.html as lh
import pandas as pd

url = 'https://www.pro-football-reference.com/play-index/pgl_finder.cgi?request=1&match=game&year_min=2018&year_max=2018&season_start=1&season_end=-1&age_min=0&age_max=99&game_type=A&league_id=&team_id=&opp_id=&game_num_min=0&game_num_max=99&week_num_min=17&week_num_max=17&game_day_of_week=&game_location=&game_result=&handedness=&is_active=&is_hof=&c1stat=rush_att&c1comp=gt&c1val=1&c2stat=&c2comp=gt&c2val=&c3stat=&c3comp=gt&c3val=&c4stat=&c4comp=gt&c4val=&order_by=rush_yds&from_link=1'
page = requests.get(url)
doc = lh.fromstring(page.content)

tr_elements = doc.xpath('//tr')

col = []
i = 0

for t in tr_elements[1]:
    i+=1
    name=t.text_content()
    print ('%d:"%s"'%(i,name))
    col.append((name,[]))

#Since out first row is the header, data is stored on the second row onwards
for j in range(2,len(tr_elements)):
    #T is our j'th row
    T=tr_elements[j]
    
    #If row is not of size x, the //tr data is not from our table 
    if len(T)!=17:
        break
    
    #i is the index of our column
    i=0
    
    #Iterate through each element of the row
    for t in T.iterchildren():
        data=t.text_content() 
        #Check if row is empty
        if i>0:
        #Convert any numerical value to integers
            try:
                data=float(data)
            except:
                pass
        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        #Increment i for the next column
        i+=1

Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)

df.to_csv('2018_RUSstats_Wk17.csv',sep=',')