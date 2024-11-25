import pandas as pd
import numpy as np

df=pd.read_excel('debi_vahed.xlsx')

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

Darsad_nadashte={}
M=d-b+1
Darsad=[]
for station in station_years.keys():
    darsad=((M-len(station_years[station]))/M)*100
    Darsad_nadashte[station]=darsad
    Darsad.append(darsad)
print(Darsad_nadashte)

data=[]
keys_list = list(Darsad_nadashte)
for i in range(0,len(keys_list),1):
    data.append([keys_list[i],Darsad[i]])

dff = pd.DataFrame(data, columns=['station code', 'Darsade nadashte'])
print(dff)
dff.to_excel('darsadedebi_nadashte.xlsx')





























