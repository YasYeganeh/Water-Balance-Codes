import pandas as pd

df=pd.read_excel('StationsHavashenasi.xlsx')
# stations=set(df['code'].tolist())
# # print(stations)
# print(len(stations))

# BARESH STATIONS
df1=pd.read_excel('هواشناسی_بارش_روزانه_حوضه ای_14.xlsx')
# print(df)
stations14_BARESH=set(df1['code'].tolist())
print('14-sefidroodharaz BARESH stations:',stations14_BARESH)
print(len(stations14_BARESH))

df1_Bareshstation=df.loc[(df['code'].isin(stations14_BARESH))]
df_coordinates=df1_Bareshstation[['code','station','ertefa','arz','tool','tasis']]
df_coordinates.to_excel('14sefidroodharaz_stations_coordinates1.xlsx')
##############################################
# TABKHIR STATIONS
df2=pd.read_excel('هواشناسی_تبخیر_روزانه_حوضه ای_14.xlsx')
# print(df)
stations14_EVAPO=set(df2['code'].tolist())
print('14-sefidroodharaz  stations:',stations14_EVAPO)
print(len(stations14_EVAPO))
print(set(stations14_BARESH).intersection(set(stations14_EVAPO)))
