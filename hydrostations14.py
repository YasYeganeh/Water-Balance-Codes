import pandas as pd

df=pd.read_excel('StationsHydrometry.xlsx')
# stations=set(df['code'].tolist())
# # print(stations)
# print(len(stations))

# HYDROMETRY STATIONS
df1=pd.read_excel('هیدرومتری_دبی_روزانه_حوضه ای_14.xlsx')
# print(df)
stations14_hydro=set(df1['code'].tolist())
print('14-sefidroodHaraz hydro stations:',stations14_hydro)
print(len(stations14_hydro))

df1_Bareshstation=df.loc[(df['CODE'].isin(stations14_hydro))]
df_coordinates=df1_Bareshstation[['CODE','STATION','RIVER','ERTEFA','ARZ','TOOL','TASIS','ESHEL','LEMINGRAPH','TELFERIK','MASAHAT','ديتالاكر']]
df_coordinates.to_excel('14sefidroodHaraz_hydrostations_coordinates1.xlsx')