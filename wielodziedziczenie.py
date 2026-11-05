"""Wielodziedziczenie, MRO i wybór klasy w super()."""
class A:
    """Klasa w łańcuchu MRO; woła następną przez super()."""
    def m1(self):
        """Wypisuje nazwę i woła następną klasę."""
        print('A.m1')
        super().m1()

class B(A):
    """Podklasa A."""
    def m1(self):
        """Wypisuje nazwę i woła następną klasę."""
        print('B.m1')
        super().m1()

class C:
    """Klasa kończąca łańcuch."""
    def m1(self):
        """Wypisuje nazwę."""
        print('C.m1')
        # super().m1()

class D(B, C):
    """Klasa dziedzicząca po B i C."""
    def m1(self):
        """Pokazuje, jak przez super() ominąć część MRO."""
        print('D.m1')
        # class one before the one we want in __mro__, self
        super(A, self).m1()
        # a bit simpler
        class_i_want = C
        i = self.__class__.__mro__.index(class_i_want) - 1
        super(self.__class__.__mro__[i], self).m1()

# for mix-in classes (domieszkowe) use them as left class in inheritace


if __name__ == "__main__":
    d = D()
    d.m1()
    print(D.__mro__)
