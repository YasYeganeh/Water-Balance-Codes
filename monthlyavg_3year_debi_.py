import pandas as pd

df=pd.read_excel('debi_vahed.xlsx')
stations=df['code'].tolist()
# print(stations)
df1=df[df['abi']==90]
# print(df1.shape[0])
# print(len(df1['mhr'].tolist()))
df2=df[df['abi']==91]
# print(df2.shape[0])
# print(len(df2['mhr'].tolist()))
df3=df[df['abi']==93]
# print(df1)

###### YAFTANE MASAHATE MOTANAZERE HAR OUTLET (EXIT STATION)

dff=pd.read_excel('mahdoudeha.xlsx')
station_mahdoude={'19-015':[1110,1111,1112],'19-043':[1106,1108,1109,1107],'19-131':[1105],'19-119':[1101,1102,1104],'19-981':[1103],'18-025':[1201],'18-083':[1202],'17-059':[1301,1303,1305,1304,1306,1309,1308,1307,1302,1310,1311],'16-057':[1401],'16-025':[1402],'16-009':[1403],'14-017':[1501],'14-007':[1502],'13-006':[1503],'12-055':[1504],'12-097':[1601,1602],'11-069':[1701],'11-073':[1703,1704,1705,1706,1707,1708],'19-001':[1113],'11-051':[1702]}
# print(len(station_mahdoude.keys()))
MAZANDARAN_area=175060
station_mahdoudearea={}
station_ratio={}
for station in station_mahdoude.keys():
    A=[]
    for i in station_mahdoude[station]:
        # print(station,i)
        area=dff.loc[dff['code'] == i, 'Area'].item()
        A.append(area)
    station_mahdoudearea[station]=sum(A)
    B=MAZANDARAN_area/sum(A)
    station_ratio[station]=B
print(station_mahdoudearea)
print(station_ratio)
# print(df2.loc[df2['code'] == 1101, 'Area'].item())

#### YAFTANE MOTEVASETE DEBI HAR OUTLET

month_avg={}
month_corrected={}
months=['mhr','abn','azr','dey','bah','esf','far','ord','khr','tir','mor','shr']
outlet_stations=['19-015','19-043','19-131','19-119','19-981','18-025','18-083','17-059','16-057','16-025','16-009','14-017','14-007','13-006','12-055','12-097','11-069','11-073','11-051','19-001']
for idx, dfi in enumerate([df1, df2, df3]):
    dfi.reset_index(inplace=True)
    print(f"Year {idx + 1}:")
    total_debi=0
    for outlet in outlet_stations:
        df0=dfi[dfi['code']==outlet]
        count_row = df0.shape[0]
        stationbadade=0
        if count_row!=0:
            stationbadade+=1
            for i in months:
                monthdatalist_nandar = df0[i].tolist()
                monthdatalist = [x for x in monthdatalist_nandar if pd.isnull(x) == False]
                # print(i,':',monthdatalist)
                avg = sum(monthdatalist) / count_row
                month_avg[i] = avg
                for key in month_avg:
                    month_corrected[key] = month_avg[key] * station_ratio[outlet]
            print(f"Monthly station {outlet}:", month_avg)
            print(f"Monthly corrected station {outlet}:", month_corrected)
            print(f"Yearly station{outlet}:", sum(month_avg.values()) / len(month_avg.values()))
            print(f"Yearly corrected station{outlet}:", sum(month_corrected.values()) / len(month_corrected.values()))
            total_debi += (sum(month_corrected.values()) / len(month_corrected.values()))
        else:
            print(f"Outlet station{outlet} has no data in year{idx + 1}")
    print(total_debi)

##### YAFTANE MASAHATE ISTGAH KE MOSHAHEDE SHOD MASAHATE HAME ISTGAH HA SABT NASHODE
# df1=pd.read_excel('StationsHydrometry.xlsx')
# area_station={}
# for i in outlet_stations:
#     area=df1[df1['CODE']==i]['MASAHAT']
#     area_station[i]=area
# print(area_station)







