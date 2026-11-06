"""Główny proces czeka przez JoinableQueue, aż wszystkie zadania zostaną wykonane."""

import multiprocessing


def konsument(kolejka):
    """Bez końca odbiera zadania i potwierdza wykonanie każdego z nich."""
    while True:
        liczba = kolejka.get()
        print(f"{liczba} do kwadratu to {liczba**2}", flush=True)
        kolejka.task_done()  # potwierdzenie: to zadanie jest zrobione


if __name__ == "__main__":
    kolejka = multiprocessing.JoinableQueue()

    # daemon=True: proces zakończy się razem z głównym, więc nie potrzeba znaku KONIEC
    p = multiprocessing.Process(target=konsument, args=(kolejka,), daemon=True)
    p.start()

    for liczba in range(1, 6):
        kolejka.put(liczba)

    kolejka.join()  # czeka, aż każde put dostanie swoje task_done
    print("wszystkie zadania wykonane")
