import numpy as np
import heapq


def g_sortujacy(lista):
    a = np.argsort(lista)
    for i in a:
        yield lista[i]


def g_sortujacy(lista):
    # na stercie binarnej
    # to skonsumuje oryginalną listę
    heapq.heapify(lista)
    while lista:
        yield heapq.heappop(lista)


x = [1, 9, 6, 3]
for w in g_sortujacy(x):
    print(w)
