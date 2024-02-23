import math

# a
# n = int(input('podaj liczbe: '))
# if n < 100:
#     for i in range(0,n+1):
#         for j in range(0,n+1):
#             print(i,'*',j,'=',i*j)
# else:
#     print('n is too large')
#
# # b
# a = int(input('podaj pierwsza liczbe: '))
# b = int(input('podaj druga liczbe: '))
# x = math.gcd(a, b)
# p = a//x
# q = b//x
# print(a/b, p/q)

# c
# n = int(input('podaj liczbe: '))
# e1 = (1+(1/n)) ** n
# e2 = 0
# for k in range(0,n+1):
#     e2 += (1/math.factorial(k))
#
# print(e1,'-',math.e)
# print(e2,'-',math.e)
# print(abs(e1),'-',abs(math.e))
# print(abs(e2),'-',abs(math.e))

# d
x = -2
y = 2
def najw_wsp_dzielnik(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

print(najw_wsp_dzielnik(x, y))
