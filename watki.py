"""Uruchamianie wątków przez threading."""
import threading
import multiprocessing
import time
from pprint import pprint

d = {}
def czekaj(n):
    """Czeka n sekund i zapisuje wynik we wspólnym słowniku."""
    print(f'Watek {threading.current_thread().name} czeka {n} sekund...\n', end='')
    time.sleep(n)
    print(f'Watek {threading.current_thread().name} konczy...\n', end='')
    d[threading.current_thread().name] = 'wynik'

if __name__ == '__main__':
    watek1 = threading.Thread(target=czekaj, args=(3,))
    watek2 = threading.Thread(target=czekaj, args=(3,))
    watek3 = threading.Thread(target=czekaj, args=(3,))
    watek4 = threading.Thread(target=czekaj, args=(3,))
    watek1.start()
    watek2.start()
    watek3.start()
    watek4.start()
    watek1.join()
    watek2.join()
    watek3.join()
    watek4.join()
    pprint(d)