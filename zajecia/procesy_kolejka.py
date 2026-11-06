"""Producent i konsument w osobnych procesach, połączeni przez multiprocessing.Queue."""

import multiprocessing
import time

KONIEC = None  # umówiony znak: nie będzie więcej zadań


def producent(kolejka):
    """Wkłada liczby do kolejki, a na końcu znak KONIEC."""
    for liczba in range(1, 6):
        print(f"producent: wkładam {liczba}", flush=True)
        kolejka.put(liczba)
        time.sleep(0.2)
    kolejka.put(KONIEC)
    print("producent: koniec", flush=True)


def konsument(kolejka):
    """Odbiera liczby z kolejki, dopóki nie dostanie znaku KONIEC."""
    while True:
        liczba = kolejka.get()  # czeka, aż coś się pojawi
        if liczba is KONIEC:
            break
        print(f"konsument: {liczba} do kwadratu to {liczba**2}", flush=True)
    print("konsument: koniec", flush=True)


if __name__ == "__main__":
    kolejka = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=producent, args=(kolejka,))
    p2 = multiprocessing.Process(target=konsument, args=(kolejka,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("główny proces: koniec")
