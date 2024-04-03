class Fruit:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def isfresh(self):
        if self.color == 'czarny':
            return False
        return True

class Apple(Fruit):
    pass

class Banana(Fruit):
    pass

class Orange(Fruit):
    pass

a = Fruit('czarny','50')
print(a.isfresh())

b = Apple('zolty','50')
print(b.isfresh())