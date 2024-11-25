import pandas as pd

df=pd.read_excel('tabkhir_vahed.xlsx')
stations=df['code'].tolist()
# print(stations)
df1=df[df['abi']==90]
df2=df[df['abi']==91]
# stations2=list(set(df2['code'].tolist()))
df3=df[df['abi']==93]

month_avg={}
months=['mhr','abn','azr','dey','bah','esf','far','ord','khr','tir','mor','shr']
for idx, dfi in enumerate([df1, df2, df3]):
    dfi.reset_index(inplace=True)
    station_count=len(list(set(dfi['code'].tolist())))
    for i in months:
        monthdatalist_nandar = dfi[i].tolist()
        monthdatalist = [x for x in monthdatalist_nandar if pd.isnull(x) == False]
        # print(len(monthdatalist))
        # print(len(monthdatalist_nandar))
        avg = sum(monthdatalist) / station_count
        month_avg[i] = avg

    print(f"Monthly df{idx + 1}:", month_avg)
    print(f"Yearly df{idx + 1}:", sum(month_avg.values()))

d90={'mhr': 126.86305732484185, 'abn': 69.47770700637, 'azr': 53.184076433120566, 'dey': 15.594267515923617, 'bah': 16.586624203821742, 'esf': 21.634394904458627, 'far': 99.8331210191092, 'ord': 119.27834394904549, 'khr': 185.88089171974633, 'tir': 235.25414012738744, 'mor': 237.71210191082739, 'shr': 140.78726114649788}
for key in d90:
    d90[key] *=  0.8
d91={'mhr': 115.47405063291251, 'abn': 38.67151898734147, 'azr': 12.64430379746842, 'dey': 15.722784810126624, 'bah': 11.65379746835448, 'esf': 23.503164556961984, 'far': 87.86962025316535, 'ord': 144.31202531645695, 'khr': 208.8341772151905, 'tir': 202.97341772152075, 'mor': 254.41518987341587, 'shr': 175.54936708860947}
d93={'mhr': 126.06516129032356, 'abn': 57.592258064516244, 'azr': 28.291612903225783, 'dey': 12.89548387096786, 'bah': 14.389677419354884, 'esf': 29.145806451612888, 'far': 83.34387096774248, 'ord': 162.79935483871137, 'khr': 207.52967741935632, 'tir': 244.49290322580524, 'mor': 272.61483870967476, 'shr': 211.90451612903394}
for key in d91:
    d91[key] *=  0.8
for key in d93:
    d93[key] *=  0.8
print(d90)
print(d91)
print(d93)
