import numpy as np

# def conv(x):
#     return x.replace(',', '.').encode()
#
# data = np.genfromtxt((conv(x) for x in open('jajka2024.csv')),delimiter=';',dtype=('|U16'),encoding='utf-8')
data = np.genfromtxt('jajka2024.csv',delimiter=';',dtype=('|U16'),encoding='utf-8')
print(data)
