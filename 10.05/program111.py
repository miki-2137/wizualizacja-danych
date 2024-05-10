import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('penguins.csv',sep=',',encoding='UTF-8')

srednia_waga = data.groupby('sex')['body_mass_g'].mean()
waga_max = data[data['body_mass_g']==data['body_mass_g'].max()]
waga_min = data[data['body_mass_g']==data['body_mass_g'].min()]
count = data.groupby(['island']).size()
count_island = data.groupby(['island']).size()

plot = count_island.plot(kind='bar',rot=0,title='pingwiny')
plt.show()

plt.scatter(data['bill_length_mm'], data['bill_depth_mm'],alpha=0.5)
plt.title('zaleznosc dlugosci od szerokosci dzioba')
plt.xlabel('dlugosc dzioba')
plt.ylabel('szerokosc dzioba')
plt.show()
