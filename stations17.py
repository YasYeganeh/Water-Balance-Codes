import pandas as pd

df=pd.read_excel('StationsHavashenasi.xlsx')
# stations=set(df['code'].tolist())
# # print(stations)
# print(len(stations))

# BARESH STATIONS
df1=pd.read_excel('هواشناسی_بارش_روزانه_حوضه ای_17.xlsx')
# print(df)
stations17_BARESH=set(df1['code'].tolist())
print('16-atrak BARESH stations:',stations17_BARESH)
print(len(stations17_BARESH))


df1_Bareshstation=df.loc[(df['code'].isin(stations17_BARESH))]
df_coordinates=df1_Bareshstation[['code','station','ertefa','arz','tool','tasis']]
df_coordinates.to_excel('17atrak_stations_coordinates1.xlsx')
##############################################
# TABKHIR STATIONS
df2=pd.read_excel('هواشناسی_تبخیر_روزانه_حوضه ای_17.xlsx')
# print(df)
stations17_EVAPO=set(df2['code'].tolist())
print('17-atrak  stations:',stations17_EVAPO)
print(len(stations17_EVAPO))
print(set(stations17_BARESH).intersection(set(stations17_EVAPO)))
