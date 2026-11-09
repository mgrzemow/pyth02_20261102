"""ProcessPoolExecutor z callbackiem (add_done_callback): obiekt wywoływalny zbiera wyniki i błędy."""

import concurrent.futures as cf
import random
import time
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
    if random.randint(1, 100) < 10:
        9 / 0  # celowy błąd w około 10% zadań
    for _ in range(m):
        fibo(10_000)
    return "wynik"


class MojFajnyCallback:
    """Callback jako obiekt z __call__: liczy zakończone zadania i zbiera wyniki."""

    def __init__(self, total):
        """Zapamiętuje, ile zadań ma się zakończyć."""
        self.lista = []
        self.total = total
        self.done = 0

    def __call__(self, future: cf.Future):
        """Wywoływany przez pulę po zakończeniu zadania; zapisuje wynik albo wyjątek."""
        try:
            self.lista.append(future.result())
        except Exception as e:
            self.lista.append(e)
        self.done += 1

    def all_done(self):
        """Mówi, czy wszystkie zadania już się zakończyły."""
        return self.done == self.total

    def __repr__(self):
        """Pokazuje postęp, np. 40/100 done."""
        return f"{self.done}/{self.total} done"


if __name__ == "__main__":
    with cf.ProcessPoolExecutor(16) as executor:
        params = [1000] * 100
        mc = MojFajnyCallback(len(params))
        futures = [executor.submit(n_times_fibo, p) for p in params]
        [f.add_done_callback(mc) for f in futures]
        while not mc.all_done():
            time.sleep(1)
            print(mc)
        pprint(mc.lista)
