"""Uruchamianie procesów przez multiprocessing."""

import multiprocessing
import time


def czekaj(n):
    """Czeka n sekund i wypisuje nazwę procesu."""
    print(
        f"Proces {multiprocessing.current_process().name} czeka {n} sekund...\n", end=""
    )
    time.sleep(n)
    print(f"Proces {multiprocessing.current_process().name} konczy...\n", end="")


if __name__ == "__main__":
    proces1 = multiprocessing.Process(target=czekaj, args=(3,))
    proces2 = multiprocessing.Process(target=czekaj, args=(3,))
    proces3 = multiprocessing.Process(target=czekaj, args=(3,))
    proces4 = multiprocessing.Process(target=czekaj, args=(3,))
    proces1.start()
    proces2.start()
    proces3.start()
    proces4.start()
    proces1.join()
    proces2.join()
    proces3.join()
    proces4.join()
