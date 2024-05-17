import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# def sinplot(flip=1):
#     x = np.linspace(0,14,100)
#     for i in range(1,5):
#         plt.plot(x,np.sin(x+i*.5)*(7-i)*flip)
# sns.set_style("whitegrid")
# sns.set_palette("husl")
# sinplot()
# print(sns.axes_style())
# plt.show()

def sinplot(flip=1):
    x = np.linspace(-2,2,100)
    for i in x:
        plt.plot(x)
        plt.plot(x,np.power(x,2))
sns.set_style("whitegrid")
sns.set_palette("husl")
sinplot()
print(sns.axes_style())
plt.show()
