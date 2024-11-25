import pandas as pd

df=pd.read_excel('allwells.xlsx')
stations=df['code'].tolist()
# print(stations)
nime1=[1,2,3,4,5,6]
nime2=[7,8,9,10,11,12]
df1389=df[(df['sal1']==1389) & (df['mah'].isin(nime2))]
df1390=df[(df['sal1']==1390) & (df['mah'].isin(nime1))]
df90=df1389.append(df1390)
# df90.to_excel('90.xlsx')
# print(df90)
df1390=df[(df['sal1']==1390) & (df['mah'].isin(nime2))]
df1391=df[(df['sal1']==1391) & (df['mah'].isin(nime1))]
df91=df1390.append(df1391)
# print(df91)
df1392=df[(df['sal1']==1392) & (df['mah'].isin(nime2))]
df1393=df[(df['sal1']==1393) & (df['mah'].isin(nime1))]
df93=df1392.append(df1393)
# print(df93)

month_avg={}
months=[7,8,9,10,11,12,1,2,3,4,5,6]
for idx, dfi in enumerate([df90, df91, df93]):
    print(f"Year {idx + 1}:")
    for i in months:
        # print(i)
        df0=dfi[dfi['mah']==i]
        count_row = df0.shape[0]
        monthdatalist_nandar = df0["sath_ab"].tolist()
        monthdatalist = [x for x in monthdatalist_nandar if pd.isnull(x) == False]
        # print(i,':',monthdatalist)
        avg = sum(monthdatalist) / count_row
        month_avg[i] = avg
    print(f"Monthly df{idx + 1}:", month_avg)
    print(f"Yearly df{idx + 1}:", sum(month_avg.values()) / len(month_avg.values()))



