import pandas as pd

df=pd.read_excel('baresh_vahed.xlsx')
stations=df['code'].tolist()
# print(stations)
df1=df[df['abi']==90]
df2=df[df['abi']==91]
# stations2=list(set(df2['code'].tolist()))
df3=df[df['abi']==93]

month_avg={}
months=['mhr','abn','azr','dey','bah','esf','far','ord','khr','tir','mor','shr']
for idx, dfi in enumerate([df1, df2, df3]):
    dfi.reset_index(inplace=True)
    station_count=len(list(set(dfi['code'].tolist())))
    for i in months:
        monthdatalist_nandar = dfi[i].tolist()
        monthdatalist = [x for x in monthdatalist_nandar if pd.isnull(x) == False]
        # print(len(monthdatalist))
        # print(len(monthdatalist_nandar))
        avg = sum(monthdatalist) / station_count
        month_avg[i] = avg
    print(f"Monthly df{idx + 1}:", month_avg)
    print(f"Yearly df{idx + 1}:",sum(month_avg.values()))


