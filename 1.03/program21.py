import math

print(math.ceil(math.sqrt(2)))
print(math.floor(math.sqrt(2)))
print(round(math.sqrt(2)))

a = 5
b = 2
def mod(x,y):
    if isinstance(x,float) or isinstance(y,float):
        return math.fmod(x,y)
    else:
        return x % y

print(mod(a,b))

def log(a,n):
    for k in range(2,n+1):
        print(math.log(a,k),end='|')
    print('\n')

log(10,10)

def pow(a):
    return math.exp(a), math.e**a, math.pow(math.e,a)

print(pow(a))

#math.pow(2,1.5) zwroci blad, 2**1.5 zwraca wynik liczbowy

#math.remainder(-2,-3) zwraca 1.0, -2%-3 zwraca -2

#math.cosh(2) = 3.7621956910836314, wynik z definicji = 3.6268604078470186

#math.sinh(2) = 3.6268604078470186, wynik z definicji = 3.762195691083631
