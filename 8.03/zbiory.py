panstwa = {'Polska','Estonia','Austria','USA','Ukraina'}
print('Polska' in panstwa)

panstwa.add('Polska')
print(panstwa)

panstwa.remove('Polska')
print(panstwa)

panstwa2 = {'Estonia'}
print(panstwa | panstwa2)
print(panstwa & panstwa2)
print(panstwa - panstwa2)
print(panstwa2.issubset(panstwa))
