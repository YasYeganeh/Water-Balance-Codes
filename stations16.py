import pandas as pd

df=pd.read_excel('StationsHavashenasi.xlsx')
# stations=set(df['code'].tolist())
# # print(stations)
# print(len(stations))

# BARESH STATIONS
df1=pd.read_excel('هواشناسی_بارش_روزانه_حوضه ای_16.xlsx')
# print(df)
stations16_BARESH=set(df1['code'].tolist())
print('16-GharehsooGorgan BARESH stations:',stations16_BARESH)
print(len(stations16_BARESH))

df1_Bareshstation=df.loc[(df['code'].isin(stations16_BARESH))]
df_coordinates=df1_Bareshstation[['code','station','ertefa','arz','tool','tasis']]
df_coordinates.to_excel('16GharehsooGorgan_stations_coordinates1.xlsx')
##############################################
# TABKHIR STATIONS
df2=pd.read_excel('هواشناسی_تبخیر_روزانه_حوضه ای_16.xlsx')
# print(df)
stations16_EVAPO=set(df2['code'].tolist())
print('16-GharehsooGorgan  stations:',stations16_EVAPO)
print(len(stations16_EVAPO))
print(set(stations16_BARESH).intersection(set(stations16_EVAPO)))
