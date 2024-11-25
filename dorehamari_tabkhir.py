import pandas as pd
import numpy as np

df=pd.read_excel('tabkhir_vahed.xlsx')

# years11 = set(df['sal'].tolist())
# print(years11)
# print(len(years11))
stations = set(df['code'].tolist())
# print(stations)
print('station count:',len(stations))

station_years={}
for i in stations:
    dff=df[df['code']==i]
    years=list(set(dff['abi'].tolist()))
    station_years[i]=years
print(station_years)

a=[]
c=[]
for i in station_years.values():
    min_val=min(i)
    a.append(min_val)
    min_val = max(i)
    c.append(min_val)
b=min(a)
d=max(c)
print("minimum sale abi ke dade mojoode:",b)
print("maximum sale abi ke dade mojoode:",d)

limitsalstations={}
UL=[]
LL=[]
for station in station_years.keys():
    minval=min(station_years[station])
    maxval=max(station_years[station])
    limitsalstations[station]=[minval,maxval]
    UL.append(minval)
    LL.append(maxval)
# print(limitsalstations)

an_array = np.empty((len(stations),d-b+1))
an_array[:] = np.NaN
# print(an_array)
df_table = pd.DataFrame(data = an_array, columns= reversed(range(b,d+1)))
# print(df_table)

row=0
names=[]
for station in stations:
    sal_abi=station_years[station]
    for year in reversed(range(b,d+1)):
        if year in sal_abi:
            df_table[year][row]=year
        else:
            df_table[year][row]=np.nan
    stationname=df.loc[df['code']==station]['station'].unique()[0]
    names.append(stationname)
    row+=1
# print(df_table)
df_table['A*']=UL
df_table['B**']=LL
df_table['station name']=names
df_table['station code']=list(stations)
# print(df_table)
# df_table.to_excel('Evapo_Table.xlsx')

























