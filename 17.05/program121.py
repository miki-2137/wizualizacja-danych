import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)
y = np.divide(1,1+x**2)
plt.plot(x,y,'green',linestyle='-',label='1/(1+x^2)')
plt.legend(title='Wykres')
plt.show()

x1 = np.linspace(0,4,100)
y1 = np.square(x1)
y2 = np.exp(x1)
y3 = np.power(x1,x1)
plt.plot(x1,y1,'green',linestyle='--',label='x^2')
plt.plot(x1,y2,'red',linestyle=':',label='e^x')
plt.plot(x1,y3,'blue',linestyle='-',label='x^x')
plt.legend(title='Wykres2')
plt.show()

x1 = np.linspace(0,4,100)
y1 = np.square(x1)
y2 = np.exp(x1)
y3 = np.power(x1,x1)
fig, (ax1,ax2,ax3) = plt.subplots(nrows=3, ncols=1)
ax1.plot(x1,y1,'green',linestyle='--',label='x^2')
ax2.plot(x1,y2,'red',linestyle=':',label='e^x')
ax3.plot(x1,y3,'blue',linestyle='-',label='x^x')
fig.legend(title='Wykres2', loc='upper center')
plt.show()

x1 = np.linspace(0,4,100)
y1 = np.square(x1)
y2 = np.exp(x1)
y3 = np.power(x1,x1)
ax1 = plt.subplot(311)
plt.plot(x1,y1,'green',linestyle='--',label='x^2')
ax2 = plt.subplot(312)
plt.plot(x1,y2,'red',linestyle=':',label='x^2')
ax3 = plt.subplot(313)
plt.plot(x1,y3,'blue',linestyle='-',label='x^2')
fig.legend(title='Wykres2', loc='upper center')
plt.show()