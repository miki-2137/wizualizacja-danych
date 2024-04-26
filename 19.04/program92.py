import pandas as pd

df1 = pd.DataFrame ([[2942,9840,2794,8891,8111,2933,8301,9125],
['Sylwia','Katarzyna','Teresa','Tomasz','Cezary','Zenon','Filip','Adrian'],
[13,31,34,14,13,28,20,15]]).T
df1.columns = ['ID','Name','Age']
print(df1)

weight = [65,80,64,69,74,61,66,61]
height = [179,179,151,177,170,157,151,153]
glasses = [False,True,False,True,False,True,False,True]
df2 = pd.DataFrame ([[2312,2336,2942,9840,2794,8891,8111,2933],
['Anna','Zofia','Sylwia','Katarzyna','Teresa','Tomasz','Cezary','Zenon'],
weight,height,glasses]).T
df2.columns = ['ID','Name','W','H','Gl']
print(df2)

df0 = pd.merge(df1,df2,on=['Name','ID'],how='inner')
print(df0)
print(df0.sort_values(by=['Name']))
print(df0[df0['Gl']])

df_wiek = df0[(df0['Age']<30)&(df0['Age']>20)]
print(df_wiek)

df0['bmi'] = (df0['W']/df0['H']**2*10000).astype(float)
print(df0)
print(df0['Age'].mean().round(2))
print(df0[df0['Gl']]['Age'].mean().round(2))
print(df0[df0['Gl']==False]['Age'].mean().round(2))
print(df0.groupby(['Gl'])['Age'].mean().astype(float).round(2))
print(df0.groupby(['Gl'])['bmi'].mean().astype(float).round(2))
