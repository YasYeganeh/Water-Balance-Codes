import pandas as pd

df=pd.read_excel('StationsHydrometry.xlsx')
# stations=set(df['CODE'].tolist())
# # print(stations)
# print(len(stations))

# HYDROMETRY STATIONS
df1=pd.read_excel('هیدرومتری_دبی_روزانه_حوضه ای_16.xlsx')
# print(df)
stations16_hydro=set(df1['code'].tolist())
print('16-GharehsooGorgan hydro stations:',stations16_hydro)
print(len(stations16_hydro))

df1_Bareshstation=df.loc[(df['CODE'].isin(stations16_hydro))]
df_coordinates=df1_Bareshstation[['CODE','STATION','RIVER','ERTEFA','ARZ','TOOL','TASIS','ESHEL','LEMINGRAPH','TELFERIK','MASAHAT','ديتالاكر']]
df_coordinates.to_excel('16GharehsooGorgan_hydrostations_coordinates1.xlsx')
