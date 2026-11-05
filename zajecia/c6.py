"""Ćwiczenie: menedżer kontekstu mierzący czas. Pomiar list i deque trwa około 25 s."""

# napisać menedżera kontekstu mierzącego czas wykonania kodu pod with
import time
import collections


class Stoper:
    """Menedżer kontekstu mierzący czas wykonania bloku with."""

    def __init__(self, msg):
        """Zapamiętuje opis pomiaru."""
        self.msg = msg

    def __enter__(self):
        """Zapisuje czas startu i zwraca stoper."""
        self.t1 = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Zapisuje czas końca; wyjątki z bloku lecą dalej."""
        self.t2 = time.perf_counter()
        # print('exit', exc_type, exc_value, traceback)

    def __repr__(self):
        """Zwraca opis pomiaru z czasem w sekundach."""
        return f"{self.msg}: {self.t2 - self.t1:0.2f} s."


if __name__ == "__main__":
    with Stoper("50 000 insertow") as s:
        x = []
        for i in range(50_000):
            x.insert(0, i)
    print(s)

    with Stoper("100 000 insertow") as s:
        x = []
        for i in range(100_000):
            x.insert(0, i)
    print(s)

    with Stoper("200 000 insertow") as s:
        x = []
        for i in range(200_000):
            x.insert(0, i)
    print(s)

    with Stoper("400 000 insertow") as s:
        x = []
        for i in range(400_000):
            x.insert(0, i)
    print(s)

    # deque wstawia na początek w czasie stałym, a lista przesuwa wszystkie elementy
    with Stoper("400 000 insertow do deque") as s:
        x = collections.deque()
        for i in range(400_000):
            x.insert(0, i)

    print(s)
