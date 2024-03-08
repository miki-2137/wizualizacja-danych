import math

liczby = [x for x in range(0,15)]
print(liczby)

potegi = [x**5 for x in liczby]
print(potegi)

silnie = [math.factorial(x) for x in range(0,21)]
print(silnie)

potegi_e = [math.e**x for x in range(0,20)]
print(potegi_e)

nazwiska = ['Nowak', 'Kowalski', 'Nowacki']
dlugosc = [len(x) for x in nazwiska]
print(dlugosc)