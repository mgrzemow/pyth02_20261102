"""Metaklasa jako funkcja dodająca atrybut do klasy."""
# napisać funkcję, która ma takie parametry jak type i
# ktora wola type

def pierwsza_metaklasa(cls_name, clas_inh, cls_dict):
    """Dodaje atrybut version, a potem tworzy klasę przez type()."""
    print('pierwsza metaklasa', cls_name, clas_inh, cls_dict)
    cls_dict['version'] = '1.2.3'
    return type(cls_name, clas_inh, cls_dict)

class A(metaclass=pierwsza_metaklasa):
    """Klasa tworzona przez funkcję metaklasy."""
    atr = 12
    def m1(self, x):
        """Przykładowa metoda."""
        print('A.m1', x)


if __name__ == "__main__":
    a = A()
    a.m1(12)
    print(a.version)
