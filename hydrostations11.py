import pandas as pd

df=pd.read_excel('StationsHydrometry.xlsx')
# stations=set(df['code'].tolist())
# # print(stations)
# print(len(stations))

# HYDROMETRY STATIONS
df1=pd.read_excel('هیدرومتری_دبی_روزانه_حوضه ای_11.xlsx')
# print(df)
stations11_hydro=set(df1['code'].tolist())
print('11-Aras hydro stations:',stations11_hydro)
print(len(stations11_hydro))

df1_Bareshstation=df.loc[(df['CODE'].isin(stations11_hydro))]
df_coordinates=df1_Bareshstation[['CODE','STATION','RIVER','ERTEFA','ARZ','TOOL','TASIS','ESHEL','LEMINGRAPH','TELFERIK','MASAHAT','ديتالاكر']]
df_coordinates.to_excel('11Aras_hydrostations_coordinates1.xlsx')
