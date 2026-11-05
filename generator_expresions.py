"""Wyrażenia generatorowe oraz pojęcia: iterable, iterator i generator."""

if __name__ == "__main__":
    x = range(10_000_000)
    # input('stop')  # pauza na podgląd zużycia pamięci w menedżerze zadań
    y1 = (i / 13 for i in x)
    print(y1)
    # input('stop')  # pauza na podgląd zużycia pamięci w menedżerze zadań
    y2 = (i * 4 for i in y1)
    print(y2)
    # input('stop')  # pauza na podgląd zużycia pamięci w menedżerze zadań
    # for i in y2:
    #     if i > 1000:
    #         break
    #     print(i)

    # naming:
    # iterable - whatever will work in for loop
    # iterator - object with __iter__ and __next__
    # generator - a kind of iterator: created by a function with yield or a generator expression

    # sometimes iterator will be separate from the iterable
    x = [1, 2, 3, 4]
    it = x.__iter__()
    print(it is x)

    # sometimes it will be the same object
    g = (i**2 for i in range(10))
    it = g.__iter__()
    print(g is it)
