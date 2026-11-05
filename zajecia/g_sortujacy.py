"""Generator zwracający elementy w kolejności: wersja z numpy i wersja ze stertą."""

import numpy as np
import heapq


def g_sortujacy(lista):
    """Wersja z numpy; nadpisana przez następną definicję."""
    a = np.argsort(lista)
    for i in a:
        yield lista[i]


def g_sortujacy(lista):
    """Wersja ze stertą; opróżnia przekazaną listę."""
    # na stercie binarnej
    # to skonsumuje oryginalną listę
    heapq.heapify(lista)
    while lista:
        yield heapq.heappop(lista)


if __name__ == "__main__":
    x = [1, 9, 6, 3]
    for w in g_sortujacy(x):
        print(w)
