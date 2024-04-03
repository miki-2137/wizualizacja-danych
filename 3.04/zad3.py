class Account:
    def __init__(self,wlasciciel,saldo):
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def saldo_koncowe(self,kwota,dzialanie):
        if dzialanie == 1:
            self.saldo += kwota
        else:
            self.saldo -= kwota
        return self.saldo

    def przelew(self,konto,kwota):
        print(self.saldo_koncowe(kwota,1))
        print(konto.saldo_koncowe(kwota,0))

    def wplata(self,kwota):
        print(self.saldo_koncowe(kwota,1))

    def wyplata(self,kwota):
        print(self.saldo_koncowe(kwota,0))

a1 = Account('Jan Nowak',1500)
a2 = Account('Piotr kowalski',3000)

print(a1.saldo)
print(a2.saldo)

a1.przelew(a2,250)
a2.przelew(a1,250)

a1.wplata(100)
a1.wyplata(100)

class PrivateAccount(Account):
    def wynagrodzenie(self,kwota):
        print(self.saldo + kwota)

class FirmAccount(Account):
    pass

