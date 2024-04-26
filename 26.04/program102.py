import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('jajka2024.csv', sep=';',index_col=0,encoding='UTF-8',decimal=',')
data2 = data.stack().astype(float)

plot = data.plot(kind='box',title='jaja')
plt.show()
plot2 = (data.T).plot(kind='box',title='ale jaja')
plt.show()
