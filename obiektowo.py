class MyClass:
    __slots__ = [
        'i_atr',
        'i_atr1',
        'i_atr2',
        'i_atr3',
    ]

    def __init__(self):
        self.i_atr3 = 12

    # class atribute
    atr = 0
    def m1(self, v):
        # instance atrubute - always on self
        self.i_atr = v

a = MyClass()
b = MyClass()

a.m1(12)
print(a.atr, b.atr)
MyClass.atr = 1
print(a.atr, b.atr)

print(a.atr, b.atr, MyClass.atr)
# this is ok
a.__class__.atr = 'new val'
print(a.atr, b.atr, MyClass.atr)

print(a.atr, b.atr, MyClass.atr)
# problemI assign class atribute on an instance
# a.asdasdasd =  123123
# a.atr = 'ooops'
print(a.atr, b.atr, MyClass.atr)

class Czlowiek:
    __slots__ = [
        'imie',
        'nazwisko',
    ]
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        print(f'Cześć, jestem {self.imie} {self.nazwisko}.')

c = Czlowiek('Ala', 'Nowak')
