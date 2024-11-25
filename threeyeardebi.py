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
# print(station_years)

c=[]
for i in station_years.values():
    min_val = max(i)
    c.append(min_val)
d=max(c)
print("maximum sale abi ke dade mojoode:",d)

year_count={}
year_range=list(range(72,d+1,1))
for year in year_range:
    # print(year)
    count=0
    for i in station_years.values():
        # print(i)
        if year in i:
            count+=1
        else:
            continue
    year_count[year]=count
# print(year_count)

from collections import Counter

k = Counter(year_count)
high = k.most_common(10)
# print("Initial Dictionary:")
# print(year_count, "\n")
print("year with 3 highest datalog:")
print("years: counts")
for i in high:
    print(i[0], " :", i[1], " ")





























