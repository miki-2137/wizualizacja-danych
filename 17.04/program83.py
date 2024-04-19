import numpy as np

np.set_printoptions(suppress=True)
panstwo = np.array(['China','Japan','Germany','USA','South Korea',
                    'India','Brazil','Mexico','Spain','Russia'])
r1999 = np.array([0.56,8.1,5.3,5.63,2.36,0.53,1.1,0.99,2.28,0.94])
r2014 = np.array([19.91,8.27,5.6,4.25,4.12,3.15,2.31,1.91,1.89,1.69])

print((r2014/r1999*100-100).round(2))

print(panstwo[max(r1999)==r1999])
print(panstwo[min(r1999)==r1999])
print(panstwo[max(r2014)==r2014])
print(panstwo[min(r2014)==r2014])

print(panstwo[r1999>r2014])
