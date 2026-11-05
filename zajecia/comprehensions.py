"""Wyrażenia listowe, słownikowe i zbiorów oraz all() i any()."""

from pprint import pprint


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = []
    for i in x:
        if i % 2 == 0:
            y.append(i**2)

    y = [i**2 for i in x if i % 2 == 0]

    all
    any

    x = ["Ola", None, "", "krawat", "Zenon", "Asia"]
    # do all the non empty strings in x which start with a capital letter
    # have a feature thet the end with an 'a'

    y = []

    for s in x:
        if s and s[0].isupper():
            y.append(s[-1] == "a")

    y = [s[-1] == "a" for s in x if s and s[0].isupper()]

    print(all(y))
    print(any(y))

    print(all(s[-1] == "a" for s in x if s and s[0].isupper()))

    print(any(s[-1] == "a" for s in x if s and s[0].isupper()))

    # multi level
    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    y = []
    for r in x:
        for e in r:
            y.append(e)
    y = [e for r in x for e in r]
    print(y)

    #
    n = 6
    m = 8
    tabliczka = []
    for i in range(1, n + 1):
        wiersz = []
        for j in range(1, m + 1):
            wiersz.append(i * j)
        tabliczka.append(wiersz)

    tabliczka = [[i * j for j in range(1, m + 1)] for i in range(1, n + 1)]

    pprint(tabliczka)

    # dict comprehension
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    d = {}
    for i in x:
        d[i] = i % 2 == 0
    # d = {key: value for i in x}
    d = {i: i % 2 == 0 for i in x}
    print(d)

    # set comprehension
    x = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]
    s = set()
    for i in x:
        s.add(i % 5)
    s = {i % 5 for i in x}
    print(s)

    x = [1, 2, 3, 4, 5]
    y = ["parzysta" if i % 2 == 0 else "nieparzysta" for i in x]
    print(y)
