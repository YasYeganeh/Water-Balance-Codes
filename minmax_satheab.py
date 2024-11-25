import pandas as pd

df=pd.read_excel('allwells.xlsx')
print('min sathe ab:',df['sath_ab'].min())
print('max sathe ab:',df['sath_ab'].max())



