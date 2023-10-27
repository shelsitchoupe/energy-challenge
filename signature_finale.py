import pandas as pd

import numpy as np
import matplotlib.pyplot as plt


"DISCLAIMER"
"ce code comporte des syntaxes trouvées sur internet , chatgpt ...."


def remp_month(time):
  for index,row in time.iterrows():
    value = time.loc[index ,'month']
  
    if value == 'janv':
        time.at[index,'month'] = 1
    if value == 'FEB':
        time.at[index,'month'] = 2

    if value == 'mars':
        time.at[index,'month'] = 3
        
    if value == 'APR':
        time.at[index,'month'] = 4   
        
        
    if value == 'MAY':
        time.at[index,'month'] = 5
        
        
    if value == 'juin':
        time.at[index,'month'] = 6
        
       
    if value == 'juil':
        time.at[index,'month'] = 7
    
    if value == 'AUG':
        time.at[index,'month'] = 8
    if value == 'sept':
        time.at[index,'month'] = 9
    if value == 'oct':
        time.at[index,'month'] = 10
    if value == 'nov':
        time.at[index,'month'] = 11  
    if value == 'DEC':
        time.at[index,'month'] = 12
  return time   

def treat_table(datas):
    
  datas['year'] = datas['DATETIME'].apply(lambda x: x.split(" ")[0].split("-")[0])
  datas['month'] = datas['DATETIME'].apply(lambda x: x.split(" ")[0].split("-")[1])
  datas['day'] = datas['DATETIME'].apply(lambda x: x.split(" ")[0].split("-")[2])
  datas['hour'] = datas['DATETIME'].apply(lambda x: x.split(" ")[1].split(":")[0])
  del datas["DATETIME"]
  datas = datas.apply(lambda x: [float(i.replace(",", ".")) for i in x])

  return datas

def add_col(time): 
  time['month'] = time['Date'].apply(lambda x: x.split(" ")[0].split("-")[1])  
  time['day'] = time['Date'].apply(lambda x: x.split(" ")[0].split("-")[0])
  del time["Date"]
  return time

time = pd.read_csv("tempout.csv" ,delimiter=";" )
datas = pd.read_csv("B12_c.csv", delimiter=";")

def adapte(time , datas):
   datas = treat_table(datas)
   time =add_col(time)
   time = remp_month(time)
   t_groupe = datas.groupby(["month", "day", "hour"]) 
   data_fin= t_groupe.mean()
   ligne,colone = data_fin.shape
   lin,col = time.shape
   time = time.iloc[:ligne]
   
   hour=np.arange(ligne) 
   return  data_fin ,time,hour

data_fin ,time2 ,hour = adapte(time,datas)
couleurs = {'H': 'red', 'W': 'blue', 'WE': 'green' ,'V': 'black'}
couleurs_plot= [couleurs[ week] for week in time2['W']]

fig, ax = plt.subplots()
pt =12
plt.title ("signature energetique B_12_a_b")
plt.ylabel("puissance de chauffage en KW ", fontsize=pt)
plt.xlabel("temperature exterieure en °C ",fontsize=pt)  
plt.scatter(time2['air_temp'], data_fin['P'], color=couleurs_plot, s=6, marker='*', label=  " 'H': 'red' , 'W': 'blue', 'WE': 'green' ,'V': 'black'' ")   
#plt.scatter(hour, data_fin['P'], color='purple', s=3, marker='*') 
plt.legend()
plt.show() 







 
time = pd.read_csv("tempout.csv" ,delimiter=";" )   
datas_38 = pd.read_csv("B38_c.csv", delimiter=";")


data_fin_38 ,time3 ,hour = adapte(time,datas_38)

couleurs = {'H': 'red', 'W': 'blue', 'WE': 'green' ,'V': 'black'}
couleurs_plot= [couleurs[ week] for week in time3['W']]
fig, ax = plt.subplots()
pt =12
plt.title ("signature energetique B_38_a_b")
plt.ylabel("puissance de chauffage en KW", fontsize=pt)
plt.xlabel("temperature exterieure en °C ",fontsize=pt) 
plt.scatter(time3['air_temp'], data_fin_38['P'], color=couleurs_plot, s=6, marker='*' ,label=  " 'H': 'red' , 'W': 'blue', 'WE': 'green' ,'V': 'black'' ")
#plt.scatter(hour, data_fin_38['P'], color='purple', s=3, marker='*')
plt.legend()
plt.show()






time = pd.read_csv("tempout.csv" ,delimiter=";" ) 
  
datas_11 = pd.read_csv("B11_c.csv", delimiter=";")
datas_fin_11 ,time4 ,hour = adapte(time,datas_11)

datas_fin_11['P']=datas_fin_11['P']-data_fin['P']
datas_fin_11['P']= datas_fin_11['P'].apply(lambda x : 0 if x < 0 else x )

couleurs = {'H': 'red', 'W': 'blue', 'WE': 'green' ,'V': 'black'}
couleurs_plot= [couleurs[ week] for week in time4['W']]
fig, ax = plt.subplots()
pt =12
plt.title ("signature energetique B_11")
plt.ylabel("puissance de chauffage en  en KW", fontsize=pt)
plt.xlabel("temperature exterieure en °C",fontsize=pt) 
plt.scatter(time4['air_temp'], datas_fin_11['P'], color=couleurs_plot, s=3, marker='*' ,label=  " 'H': 'red' , 'W': 'blue', 'WE': 'green' ,'V': 'black'' ")
#.scatter(hour, datas_fin_11['P'], color='purple', s=3, marker='*')
plt.legend()
plt.show()






