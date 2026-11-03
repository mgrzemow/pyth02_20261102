# def function_name(parameters):
#     code
#     return value

def f1(x, y):
    print('f1', x, y)


# no overloading
# second defininition overwrites the first one
def f1(x):
    print('f1', x)


# if you really want: singledispatch, multimethod

# LEGB rule

# __name__ = 'global name'
def f2():
    # __name__ = 'enclosing name'
    def f2_1():
        # __name__ = 'local name'
        print('f2', __name__)

    f2_1()


# f2()

# closures
def f3():
    x = 99
    y = 33
    lista_funkcji = []
    for i in range(3):
        def f3_1():
            print('f3', i)

        lista_funkcji.append(f3_1)
    # closure jest budowane na koniec funjkcji, gdzie i == 2
    return lista_funkcji


lf = f3()
lf[0]()
lf[1]()
lf[2]()


def f3():
    x = 99
    y = 33
    lista_funkcji = []
    for i in range(3):
        def f3_1(i=i):
            print('f3', i)

        lista_funkcji.append(f3_1)
    # closure jest budowane na koniec funjkcji, gdzie i == 2
    return lista_funkcji


# lf  = f3()
# lf[0]()
# lf[1]()
# lf[2]()

def f4(x, y, a=11, b=22):
    print(f'{x=}, {y=}')
    print(f'{a=}, {b=}')


# f4(1, 2, a=3)


# zabraniam przekazywania parametrow keyword po kolejnosci
def f5(x, y, *, c=33, a=11, b=22):
    print(f'{x=}, {y=}')
    print(f'{a=}, {b=}')


# f5(1, 2, 3)

def f6(x, y, *args, a=11, b=22):
    print(f'{x=}, {y=}')
    print(f'{args=}')
    print(f'{a=}, {b=}')


# f6(1, 2, 3, 4, 5, 5, 5, 5, 4, 4, 3, 3, 3, b=999)


def f7(x, y, *args, a=11, b=22, **kwargs):
    print(f'{x=}, {y=}')
    print(f'{args=}')
    print(f'{a=}, {b=}')
    print(f'{kwargs=}')

# f7(1,2,3,4,5,6,7,8,9, b=99, c=999, d=888, e=666)
# f7(1,2)

def f8(*args, **kwargs):
    print(f'{args=}')
    print(f'{kwargs=}')

# f8(1,2,3,4,5,6,7,8,9, b=99, c=999, d=888, e=666)
# f8()

def f9(*args, **kwargs):
    print(f'{args=}')
    print(f'{kwargs=}')
    return 42

def f9(slowo):
    return slowo[-1]

x = ['grog', 'az', 'zebra']
x.sort(key=f9)
print(x)

def print_n_times(*args, n_times=1, **kwargs):
    for _ in range(n_times):
        print(*args, **kwargs)


print_n_times(1,2,3,4,3,3,2, sep=' - ', n_times=3)

# required keyword arguments
def f10(x, y, *, a, b):
    print(f'{x=}, {y=}')
    print(f'{a=}, {b=}')

f10(1,2,a=3,b=4)

class A:
    def m1(self, *, a, b):
        print(f'A.m1 {a=}, {b=}')

class B(A):
    def m1(self, *, c, **kwargs):
        super().m1(**kwargs)
        print(f'C.m1 {c=}')
