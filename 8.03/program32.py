import math

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(list1 + list2)
wek = [list1[i]+list2[i] for i in range(len(list1))]
print(wek)

miesiace = ['marzec','maj','grudzien','luty']
num = {'styczen':1, 'luty':2, 'marzec':3, 'kwiecien':4, 'maj':5, 'czerwiec':6, 'lipiec':7, 'sierpien':8,
       'wrzesien':9, 'pazdziernik':10, 'listopad':11, 'grudzien':12}
def miesiace_sort(lista):
    mies_sort = [num[i] for i in lista]
    mies_sort.sort()
    nazwy = [i for i in num.keys()]
    mies_sort = [nazwy[i-1] for i in mies_sort]
    return mies_sort

print(miesiace_sort(miesiace))

nazwiska = ['Nowak', 'Kowalski', 'Nowacki']
def pozniejsza_litera(lista, litera):
    nazwiska_n = [i for i in lista if ord(i[0])>ord(litera)]
    return nazwiska_n

print(pozniejsza_litera(nazwiska, 'K'))

def dlugosc_nazwisk(lista):
    nazwiska_dl = [i for i in lista if len(i)>6]
    return nazwiska_dl

print(dlugosc_nazwisk(nazwiska))

def sprawdz_sort(lista):
    x = [i for i in lista]
    lista.sort(reverse=True)
    if x != lista:
        return False
    return True

print(sprawdz_sort([4,3,2]))
print(sprawdz_sort([1,2,3,4]))

def potega_listy(lista):
    potegi = [x**3 for x in lista]
    return potegi

print(potega_listy([1,2,3,4]))
print(potega_listy([5,10,1,8]))

n2 = float(input('podaj liczbe: '))
def func(list,n1,n2):
    new_list = [x if x != n1 else n2 for x in list]
    return new_list

print(func([1,4,6,9,5,12,4,4,14],4,n2))

def func2(list,n1,n2):
    new_list2 = [n2 if math.isclose(x,n1)==True else x for x in list]
    return new_list2

print(func2([1,4,6,9,5,12,4,4,14],4.0000000001,n2))