import numpy as np

# my_array = np.array([x for x in range(10,39,2)])
my_array = np.arange(10,39,2)
print(my_array)
print(my_array.shape)

my_array=my_array+3
my_array=my_array*2

my_array_div2 = np.array([x if x%6!=2 else 0 for x in my_array ])
print(my_array_div2)

def change(A,x):
    B = np.array([i if i!=0 else x for i in A])
    return B

A=np.array([1,0,3,4,0])
print(change(A,7))