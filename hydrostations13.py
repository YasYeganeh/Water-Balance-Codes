import pandas as pd

df=pd.read_excel('StationsHydrometry.xlsx')
# stations=set(df['code'].tolist())
# # print(stations)
# print(len(stations))

# HYDROMETRY STATIONS
df1=pd.read_excel('هیدرومتری_دبی_روزانه_حوضه ای_13.xlsx')
# print(df)
stations13_hydro=set(df1['code'].tolist())
print('13-sefidroodbozorg hydro stations:',stations13_hydro)
print(len(stations13_hydro))

df1_Bareshstation=df.loc[(df['CODE'].isin(stations13_hydro))]
df_coordinates=df1_Bareshstation[['CODE','STATION','RIVER','ERTEFA','ARZ','TOOL','TASIS','ESHEL','LEMINGRAPH','TELFERIK','MASAHAT','ديتالاكر']]
df_coordinates.to_excel('13sefidroodbozorg_hydrostations_coordinates1.xlsx')
