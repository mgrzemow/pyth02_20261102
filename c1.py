import collections

tekst = "ala alicja alina beata bartek"
{
    'a': ['ala', 'alicja', 'alina'],
    'b': ['beata', 'bartek'],
}

d = {}

# for slowo in tekst.split():
#     pl = slowo[0]
#     if pl not in d:
#         d[pl] = []
#     d[pl].append(slowo)


# for slowo in tekst.split():
#     pl = slowo[0]
#     lista = d.get(pl, [])
#     lista.append(slowo)
#     d[pl] = lista


# for slowo in tekst.split():
#     pl = slowo[0]
#     lista = d.setdefault(pl, []).append(slowo)
#
def rob_liste():
    return []

#

d = collections.defaultdict(list)

for slowo in tekst.split():
    pl = slowo[0]
    w = d[pl]
    w.append(slowo)
print(d)

# .get
# .setdefault
# defaultdict

x = [1,8,3,9,5,72]
y = x.sort()
print(y)

x = 9

def ustaw():
    # global x
    x = 7
    print("w funkcji:", x)
    return x




def dodaj_do_koszyka(produkt, koszyk=None):
    if koszyk is None:
        koszyk = []
    koszyk.append(produkt)
    return koszyk

print(dodaj_do_koszyka("jabłko"))
print(dodaj_do_koszyka("gruszka"))

# import math
# math.sqrt()
# from math import sqrt
# sqrt()





x = ustaw()
print("poza funkcją:", x)