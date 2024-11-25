import pandas as pd

df=pd.read_excel('allwells.xlsx')
########################
# CHAH HA CODE NADARAND! AZ ROOYE MOKHTASATESHAN DO TEDADE MOTAFAVET BEDAST MIYAYAD

wellsy=list(set(df['utmy'].tolist()))
wellsx=list(set(df['utmx'].tolist()))
# print(wells)
print('well count:',len(wellsy))
print('well count:',len(wellsx))

years=list(set(df['sal1'].tolist()))
print(f'az sale {min(years)} ta sale {max(years)} ')
print(f'az sale abi {min(years)-1300+1} ta sale abi {max(years)-1300+1} ')
