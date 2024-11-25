import pandas as pd

df=pd.read_excel('StationsHavashenasi.xlsx')
# stations=set(df['code'].tolist())
# # print(stations)
# print(len(stations))

# BARESH STATIONS
df1=pd.read_excel('هواشناسی_بارش_روزانه_حوضه ای_15.xlsx')
# print(df)
stations15_BARESH=set(df1['code'].tolist())
print('15-harazGharehsoo BARESH stations:',stations15_BARESH)
print(len(stations15_BARESH))

df1_Bareshstation=df.loc[(df['code'].isin(stations15_BARESH))]
df_coordinates=df1_Bareshstation[['code','station','ertefa','arz','tool','tasis']]
df_coordinates.to_excel('15harazGharehsoo_stations_coordinates1.xlsx')
##############################################
# TABKHIR STATIONS
df2=pd.read_excel('هواشناسی_تبخیر_روزانه_حوضه ای_15.xlsx')
# print(df)
stations15_EVAPO=set(df2['code'].tolist())
print('15-harazGharehsoo  stations:',stations15_EVAPO)
print(len(stations15_EVAPO))
print(set(stations15_BARESH).intersection(set(stations15_EVAPO)))
