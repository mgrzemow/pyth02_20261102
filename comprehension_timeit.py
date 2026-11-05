"""Porównanie czasu pętli i wyrażenia listowego przez timeit; trwa kilka sekund."""
import timeit
def policz_petla():
    """Liczy kwadraty w zwykłej pętli."""
    y = []
    for i in range(100_000):
        y.append(i**2)
    return y

def policz_comprehension():
    """Liczy kwadraty w wyrażeniu listowym."""
    y = [i**2 for i in range(100_000)]
    return y


if __name__ == "__main__":
    print(timeit.timeit('policz_petla()', globals=globals(), number=1000))
    print(timeit.timeit('policz_comprehension()', globals=globals(), number=1000))
