def dekorator(klasa):
    def m1(self, x, y):
        print('m1', x, y)
        self.m2()

    klasa.atr = 123
    klasa.m1 = m1
    return klasa


# @dekorator
class A:
    def m2(self):
        print('m2')
    ...



A = dekorator(A)

if __name__ == '__main__':
    print(A.atr)
    a = A()
    a.m1(1, 2)
