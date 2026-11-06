import concurrent.futures as cf
import random
from pprint import pprint


def fibo(n):
    """Liczy wyraz ciągu Fibonacciego iteracyjnie; zadanie obciążające procesor."""
    # 1 1 2 3 5 8 13 21
    x1 = x2 = 1

    for _ in range(n - 1):
        x1, x2 = x2, x1 + x2
    return x2


def n_times_fibo(m):
    """Liczy Fibonacciego m razy."""
    for _ in range(m):
        fibo(10_000)
    if random.randint(1, 100) < 10:
        9/0
    return 'wynik'

# if __name__ == '__main__':
#     with cf.ProcessPoolExecutor(16) as executor:
#         params = [1000] * 100
#         it = executor.map(n_times_fibo, params)
#         for w in executor.map(n_times_fibo, params):
#             print(w)


import concurrent.futures as cf
import random
from pprint import pprint


def fibo(n):
    """Liczy wyraz ciągu Fibonacciego iteracyjnie; zadanie obciążające procesor."""
    # 1 1 2 3 5 8 13 21
    x1 = x2 = 1

    for _ in range(n - 1):
        x1, x2 = x2, x1 + x2
    return x2


def n_times_fibo(m):
    """Liczy Fibonacciego m razy."""
    for _ in range(m):
        fibo(10_000)
    if random.randint(1, 100) < 10:
        9 / 0
    return 'wynik'


if __name__ == '__main__':
    with cf.ProcessPoolExecutor(16) as executor:
        params = [1000] * 100
        futures = [executor.submit(n_times_fibo, p) for p in params]
        lista_wynikow = []
        for f in cf.as_completed(futures):
            try:
                lista_wynikow.append(f.result())
            except Exception as e:
                lista_wynikow.append(e)
        pprint(lista_wynikow)
