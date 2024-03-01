import re

napis = 'W Roku Pańskim 1345, władca Henryk 12, na rzecz swoich 143209 poddanych uchwalił dekret o 20 procentowej zniżce podatków'

liczby = re.findall('[-]?\d+', napis)

def suma(liczby):
    su = 0
    for i in liczby:
        su += int(i)
    return su

print(suma(liczby))