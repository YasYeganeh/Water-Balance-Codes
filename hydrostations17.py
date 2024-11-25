import pandas as pd

df=pd.read_excel('StationsHydrometry.xlsx')
# stations=set(df['CODE'].tolist())
# # print(stations)
# print(len(stations))

# HYDROMETRY STATIONS
df1=pd.read_excel('هیدرومتری_دبی_روزانه_حوضه ای_17.xlsx')
# print(df)
stations17_hydro=set(df1['code'].tolist())
print('17-Atrak hydro stations:',stations17_hydro)
print(len(stations17_hydro))

df1_Bareshstation=df.loc[(df['CODE'].isin(stations17_hydro))]
df_coordinates=df1_Bareshstation[['CODE','STATION','RIVER','ERTEFA','ARZ','TOOL','TASIS','ESHEL','LEMINGRAPH','TELFERIK','MASAHAT','ديتالاكر']]
df_coordinates.to_excel('17Atrak_hydrostations_coordinates1.xlsx')
