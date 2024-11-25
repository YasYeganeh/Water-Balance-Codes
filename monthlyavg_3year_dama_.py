import pandas as pd

df=pd.read_excel('dama_vahed.xlsx')
stations=df['code'].tolist()
# print(stations)
df1=df[df['abi']==90]
# print(df1.shape[0])
# print(len(df1['mhr'].tolist()))
df2=df[df['abi']==91]
# print(df2.shape[0])
# print(len(df2['mhr'].tolist()))
df3=df[df['abi']==93]
# print(df1)

month_avg={}
months=['mhr','abn','azr','dey','bah','esf','far','ord','khr','tir','mor','shr']
for idx, dfi in enumerate([df1, df2, df3]):
    dfi.reset_index(inplace=True)
    count_row = dfi.shape[0]
    for i in months:
        monthdatalist_nandar=dfi[i].tolist()
        monthdatalist=[x for x in monthdatalist_nandar if pd.isnull(x) == False]
        # print(i,':',monthdatalist)
        avg=sum(monthdatalist)/count_row
        month_avg[i]=avg
    print(f"Monthly df{idx + 1}:" ,month_avg)
    print(f"Yearly df{idx + 1}:", sum(month_avg.values()) / len(month_avg.values()))


