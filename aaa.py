class Romanian:
    def __init__(self,liczba):
        self.values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        self.roman = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        self.romanian = liczba
        self.decimal = self.rom_to_dec()

    def rom_to_dec(self):
        dec = 0
        wartosci = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        for i in range(len(self.romanian)):
            akt = wartosci[self.romanian[i]]
            if i + 1 < len(self.romanian) and wartosci[self.romanian[i + 1]] > akt:
                dec -= akt
            else:
                dec += akt
        return dec
    def dec_to_rom(self, oblicz):
        wynik = []
        for i in range(len(self.values)):
            licz = int(oblicz / self.values[i])
            wynik.append(self.roman[i] * licz)
            oblicz -= self.values[i] * licz
        return ''.join(wynik)
    def __add__(self, r2):
        return self.dec_to_rom(self.decimal+r2.decimal)
    def __sub__(self, r2):
        return self.dec_to_rom(self.decimal-r2.decimal)
    def __mul__(self, r2):
        return self.dec_to_rom(self.decimal*r2.decimal)
    def __len__(self):
        return len(self.romanian)
a = Romanian("L")
b = Romanian("IXX")
print(a.decimal)
print(a+b)
print(a-b)
print(a*b)
