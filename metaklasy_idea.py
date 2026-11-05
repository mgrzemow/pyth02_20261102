"""Tworzenie klasy instrukcją class i wywołaniem type()."""
class A:
    """Klasa utworzona instrukcją class."""
    atr = 12
    def m1(self, x):
        """Przykładowa metoda."""
        print('A.m1', x)

# type(cls_name, clas_inh, cls_dict)
def m1(self, x):
    """Funkcja, która zostanie metodą klasy tworzonej przez type()."""
    print('A.m1', x)


if __name__ == "__main__":
    a = A()
    a.m1(1)
    print(a.atr)
    print(A)
    d = {
        'atr': 12,
        'm1': m1,
    }

    NewA = type('NewA', (), d)

    a = NewA()
    a.m1(1)
    print(a.atr)
    print(NewA)
