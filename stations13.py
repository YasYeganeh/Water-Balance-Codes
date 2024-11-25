import pandas as pd

df=pd.read_excel('StationsHavashenasi.xlsx')
# stations=set(df['code'].tolist())
# # print(stations)
# print(len(stations))

# BARESH STATIONS
df1=pd.read_excel('هواشناسی_بارش_روزانه_حوضه ای_13.xlsx')
# print(df)
stations13_BARESH=set(df1['code'].tolist())
print('13-sefidroodbozorg BARESH stations:',stations13_BARESH)
print(len(stations13_BARESH))

df1_Bareshstation=df.loc[(df['code'].isin(stations13_BARESH))]
df_coordinates=df1_Bareshstation[['code','station','ertefa','arz','tool','tasis']]
df_coordinates.to_excel('13sefidroodbozorg_stations_coordinates1.xlsx')
##############################################
# TABKHIR STATIONS
df2=pd.read_excel('هواشناسی_تبخیر_روزانه_حوضه ای_13.xlsx')
# print(df)
stations13_EVAPO=set(df2['code'].tolist())
print('13-sefidroodbozorg  stations:',stations13_EVAPO)
print(len(stations13_EVAPO))
print(set(stations13_BARESH).intersection(set(stations13_EVAPO)))
