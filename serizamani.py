import pandas as pd

df=pd.read_excel('هواشناسی_بارش_روزانه_حوضه ای_11.xlsx')

years = set(df['sal'].tolist())
# print(years)
Years=[]
for i in list(years):
    if i >= 1371 :
        Years.append(i)
print(Years)

headers = ['year', 'month', 'day', 'abi', 'ID', 'amount']
nimeh1=[]
a=[22,20,18,16,14,12]
for i in a:
    nimeh1.append(str(df.columns[i]))
# print(nimeh1)

nimeh2=[]
b=[34,32,30,28,26,24]
for i in b:
    nimeh2.append(str(df.columns[i]))
# print(nimeh2)
# print(str(df.columns[34]))

df11 = pd.DataFrame(columns=headers)

for i in Years:
    tdf = df[df['sal'] == i]

    for j in nimeh2:
        for k in tdf['rooz'].tolist():
            tdfd = tdf[tdf['rooz']== k]
            gen = pd.DataFrame([[f'13{i-1}',j,k,i,tdfd['ID'].tolist()[0],tdfd[j].tolist()[0]]],columns=headers)
            ndf = pd.concat([df11, gen])

    for j in nimeh1:
        for k in tdf['rooz'].tolist():
            tdfd = tdf[tdf['rooz']== k]
            gen = pd.DataFrame([[f'13{i}',j,k,i,tdfd['ID'].tolist()[0],tdfd[j].tolist()[0]]],columns=headers)
            ndf = pd.concat([df11, gen])

print(df11)
df11.to_csv('11_baresh_serizamani.csv', index=False)