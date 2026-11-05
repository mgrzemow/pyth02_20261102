"""Pomiary wątków i procesów; symulowane I/O bez ruchu w sieci, trwa kilkanaście sekund."""

import multiprocessing
import threading
import time
import timeit


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


def symuluj_io(n):
    """Udaje n operacji czekania na sieć, bez ruchu w sieci."""
    for _ in range(n):
        time.sleep(0.05)  # udaje czekanie na odpowiedź z sieci


def run_in_parallel_thread(n_threads, n_operations, f):
    """Dzieli operacje między wątki, uruchamia je i czeka na koniec."""
    op = n_operations // n_threads
    lista = []
    for _ in range(n_threads):
        # stworzyć n wątków
        lista.append(threading.Thread(target=f, args=(op,)))
    for t in lista:
        # każdy wątek uruchomić z n_operations // n_threads
        t.start()
    for t in lista:
        # zaczekać na koniec
        t.join()


def run_in_parallel_process(n_processes, n_operations, f):
    """Dzieli operacje między procesy, uruchamia je i czeka na koniec."""
    op = n_operations // n_processes
    lista = []
    for _ in range(n_processes):
        # stworzyć n procesów
        lista.append(multiprocessing.Process(target=f, args=(op,)))
    for t in lista:
        # każdy proces uruchomić z n_operations // n_threads
        t.start()
    for t in lista:
        # zaczekać na koniec
        t.join()


if __name__ == "__main__":
    for n in [32, 64, 128, 256]:
        t = timeit.timeit(
            stmt=f"run_in_parallel_thread({n}, 4096, symuluj_io)",
            globals=globals(),
            number=1,
        )
        print(f"{n}: {t:.2f}")
