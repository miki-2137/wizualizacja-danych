class Car:
    def __init__(self, marka, rok):
        self.marka = marka
        self.rok = rok


car1 = Car('Peugeot',2003)
car2 = Car('BMW',2020)

print(car1.marka,car1.rok)
print(car2.marka,car2.rok)

car1 = car2
print(car1.marka,car1.rok)
print(car2.marka,car2.rok)