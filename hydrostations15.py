import pandas as pd

df=pd.read_excel('StationsHydrometry.xlsx')
# stations=set(df['CODE'].tolist())
# # print(stations)
# print(len(stations))

# HYDROMETRY STATIONS
df1=pd.read_excel('هیدرومتری_دبی_روزانه_حوضه ای_15.xlsx')
# print(df)
stations15_hydro=set(df1['code'].tolist())
print('15-HarazGharehsoo hydro stations:',stations15_hydro)
print(len(stations15_hydro))

df1_Bareshstation=df.loc[(df['CODE'].isin(stations15_hydro))]
df_coordinates=df1_Bareshstation[['CODE','STATION','RIVER','ERTEFA','ARZ','TOOL','TASIS','ESHEL','LEMINGRAPH','TELFERIK','MASAHAT','ديتالاكر']]
df_coordinates.to_excel('15HarazGharehsoo_hydrostations_coordinates1.xlsx')
