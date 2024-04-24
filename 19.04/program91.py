import pandas as pd
import numpy as np

liczby = pd.Series([1,2,3,4])

stringi = pd.Series(['a','b','c','d'])

lista = [1,2,3,4,5]
seria = pd.Series(lista)

lista2 = stringi.to_list()
print(lista2)

tab = np.array([1,2,3])
seria2 = pd.Series(tab)
print(seria2)

tab2 = liczby.to_numpy()
print(tab2)

