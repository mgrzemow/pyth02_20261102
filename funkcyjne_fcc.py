import collections


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


d = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': lambda x, y: x / y,
}

# x1, op, x2 = input('Podaj wyrazenie: ').split()
# x1, x2 = float(x1), float(x2)

# print(d[op](x1, x2))
# print(eval(input('Podaj wyrazenie: ')))

# map filter reduce
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def f1(i):
    return i ** 2


# print(list(map(f1, x)))

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def f2(i):
    return i % 2 == 1


# print(list(filter(f2, x)))

# print(list(filter(lambda i: i % 2 == 1, x)))

# reduce
import functools


def f3(akronim, slowo):
    return akronim + slowo[0]


x = 'potrzebuje ygrekow to honorowa ogromna nadzieja'

# print(functools.reduce(f3, x.split(), ''))

x = 'ala alicja alina beata bartek'

{
    'a': ['ala', 'alicja', 'alina'],
    'b': ['beata', 'bartek']
}


# * użyć defaultdict
def f4(slownik, slowo):
    slownik[slowo[0]].append(slowo)
    print(slownik)
    return slownik


# print(functools.reduce(f4, x.split(), collections.defaultdict(list)))

# 1 1 2 3 5 8 13 21
@functools.lru_cache(maxsize=None)
def fibo(n):
    if n < 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

# print(fibo(1900))

def do_potegi(podstawa, wykladnik):
    print('do potegi', podstawa, wykladnik)
    return podstawa ** wykladnik

def do_kwadratu(podstawa):
    return do_potegi(podstawa, 2)

do_kwadratu = functools.partial(do_potegi, wykladnik=2)

print(do_kwadratu(3))

functools

print(do_potegi.__call__(2, 3))
