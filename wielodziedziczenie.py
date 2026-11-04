class A:
    def m1(self):
        print('A.m1')
        super().m1()

class B(A):
    def m1(self):
        print('B.m1')
        super().m1()

class C:
    def m1(self):
        print('C.m1')
        # super().m1()

class D(B, C):
    def m1(self):
        print('D.m1')
        # class one before the one we want in __mro__, self
        super(A, self).m1()
        # a bit simpler
        class_i_want = C
        i = self.__class__.__mro__.index(class_i_want) - 1
        super(self.__class__.__mro__[i], self)

# for mix-in classes (domieszkowe) use them as left class in inheritace

d = D()
d.m1()
print(D.__mro__)
