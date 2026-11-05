"""Funkcje jako obiekty: map, filter, reduce, lru_cache i partial."""
import collections


def add(x, y):
    """Dodaje."""
    return x + y


def sub(x, y):
    """Odejmuje."""
    return x - y


def mul(x, y):
    """Mnoży."""
    return x * y


def div(x, y):
    """Dzieli."""
    return x / y



# x1, op, x2 = input('Podaj wyrazenie: ').split()
# x1, x2 = float(x1), float(x2)

# print(d[op](x1, x2))
# print(eval(input('Podaj wyrazenie: ')))



def f1(i):
    """Zwraca kwadrat; funkcja dla map."""
    return i ** 2


# print(list(map(f1, x)))



def f2(i):
    """Sprawdza nieparzystość; funkcja dla filter."""
    return i % 2 == 1


# print(list(filter(f2, x)))

# print(list(filter(lambda i: i % 2 == 1, x)))

# reduce
import functools


def f3(akronim, slowo):
    """Dokleja pierwszą literę słowa; funkcja dla reduce."""
    return akronim + slowo[0]



# print(functools.reduce(f3, x.split(), ''))




# * użyć defaultdict
def f4(slownik, slowo):
    """Dopisuje słowo do listy pod jego pierwszą literą; funkcja dla reduce."""
    slownik[slowo[0]].append(slowo)
    print(slownik)
    return slownik


# print(functools.reduce(f4, x.split(), collections.defaultdict(list)))

# 1 1 2 3 5 8 13 21
@functools.lru_cache(maxsize=None)
def fibo(n):
    """Liczy wyraz ciągu Fibonacciego rekurencyjnie, z pamięcią wyników."""
    if n < 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

# print(fibo(1900))

def do_potegi(podstawa, wykladnik):
    """Podnosi podstawę do potęgi."""
    print('do potegi', podstawa, wykladnik)
    return podstawa ** wykladnik

def do_kwadratu(podstawa):
    """Podnosi do kwadratu; niżej nadpisana wersją z partial."""
    return do_potegi(podstawa, 2)


if __name__ == "__main__":
    d = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': lambda x, y: x / y,
    }
    # map filter reduce
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = 'potrzebuje ygrekow to honorowa ogromna nadzieja'
    x = 'ala alicja alina beata bartek'
    {
        'a': ['ala', 'alicja', 'alina'],
        'b': ['beata', 'bartek']
    }
    do_kwadratu = functools.partial(do_potegi, wykladnik=2)

    print(do_kwadratu(3))

    functools

    print(do_potegi.__call__(2, 3))
