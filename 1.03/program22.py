string = 'qwertyuiop'
string2 = 'kot'
def parzyste(s):
    print(s[::2])

parzyste(string)

n = int(input('podaj liczbe znakow: '))
def ostatnie(s, n=1):
    print(s[-n:])

ostatnie(string,n)

def odwrotny(s):
    return s[::-1]

print(odwrotny(string))

def palindrom(s):
    if s == odwrotny(s):
        return True
    return False

print(palindrom(string))

def dluzszy(s,s2):
    if len(s)>len(s2):
        print('pierwszy string jest dluzszy')
    elif len(s)<len(s2):
        print('drugi string jest dluzszy')
    else:
        print('stringi sa rowne')

dluzszy(string, string2)


imie = input('podaj imie: ')
data = input('podaj date urodzenia: ')
def dane(i,d):
    print('My name is {}. My date of birth is {}.'.format(i,d))

dane(imie,data)
