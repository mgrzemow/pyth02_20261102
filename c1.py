"""Grupowanie słów w słowniku, pułapka sort() oraz zmienne lokalne i globalne."""
import collections



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
    """Zwraca pustą listę: fabryka, którą można przekazać do defaultdict."""
    return []

#



# .get
# .setdefault
# defaultdict



def ustaw():
    """Ustawia zmienną lokalną x i zwraca ją; globalne x pozostaje bez zmian."""
    # global x
    x = 7
    print("w funkcji:", x)
    return x




def dodaj_do_koszyka(produkt, koszyk=None):
    """Dodaje produkt do koszyka; None jako wartość domyślna daje za każdym razem nową listę."""
    if koszyk is None:
        koszyk = []
    koszyk.append(produkt)
    return koszyk


if __name__ == "__main__":
    tekst = "ala alicja alina beata bartek"
    {
        'a': ['ala', 'alicja', 'alina'],
        'b': ['beata', 'bartek'],
    }
    d = {}
    d = collections.defaultdict(list)
    for slowo in tekst.split():
        pl = slowo[0]
        w = d[pl]
        w.append(slowo)
    print(d)
    x = [1,8,3,9,5,72]
    y = x.sort()  # sort działa w miejscu i zwraca None
    print(y)
    x = 9
    print(dodaj_do_koszyka("jabłko"))
    print(dodaj_do_koszyka("gruszka"))

    # import math
    # math.sqrt()
    # from math import sqrt
    # sqrt()





    x = ustaw()
    print("poza funkcją:", x)
