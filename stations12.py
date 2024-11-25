import pandas as pd

df=pd.read_excel('StationsHavashenasi.xlsx')
# stations=set(df['code'].tolist())
# # print(stations)
# print(len(stations))

# BARESH STATIONS
df1=pd.read_excel('هواشناسی_بارش_روزانه_حوضه ای_12.xlsx')
# print(df)
stations12_BARESH=set(df1['code'].tolist())
print('12-talshmordabanzali BARESH stations:',stations12_BARESH)
print(len(stations12_BARESH))


df1_Bareshstation=df.loc[(df['code'].isin(stations12_BARESH))]
df_coordinates=df1_Bareshstation[['code','station','ertefa','arz','tool','tasis']]
df_coordinates.to_excel('12taleshMordabanzali_stations_coordinates1.xlsx')
##############################################
# TABKHIR STATIONS
df2=pd.read_excel('هواشناسی_تبخیر_روزانه_حوضه ای_12.xlsx')
# print(df)
stations12_EVAPO=set(df2['code'].tolist())
print('12-talshmordab  stations:',stations12_EVAPO)
print(len(stations12_EVAPO))
print(set(stations12_BARESH).intersection(set(stations12_EVAPO)))
