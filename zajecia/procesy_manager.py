import multiprocessing
import time


def czekaj(n, d, l, v):
    """Czeka n sekund i wypisuje nazwę procesu."""
    print(f"Proces {multiprocessing.current_process().name} czeka {n} sekund...\n", end="")
    time.sleep(n)
    d[multiprocessing.current_process().name] = "wynik"
    l.append(multiprocessing.current_process().name)
    v.value += 1
    print(f"Proces {multiprocessing.current_process().name} konczy...\n", end="")


if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        d = manager.dict()
        l  = manager.list()
        v = manager.Value("i", 0)
        q = manager.Queue() # faster but you have to develop code around it

        proces1 = multiprocessing.Process(target=czekaj, args=(3,d,l,v))
        proces2 = multiprocessing.Process(target=czekaj, args=(3,d,l,v))
        proces3 = multiprocessing.Process(target=czekaj, args=(3,d,l,v))
        proces4 = multiprocessing.Process(target=czekaj, args=(3,d,l,v))
        proces1.start()
        proces2.start()
        proces3.start()
        proces4.start()
        proces1.join()
        proces2.join()
        proces3.join()
        proces4.join()
        print(d, l, v.value)
