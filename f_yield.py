"""Funkcje z yield: leniwe wykonanie w porównaniu ze zwykłą funkcją."""
def f1(n):
    """Zwykła funkcja: najpierw liczy wszystko, potem zwraca listę."""
    y = []
    for i in range(n):
        print('produkuje', i)
        y.append(i)
    return y

def f2(n):
    """Generator: produkuje wartości dopiero na żądanie."""
    print('start generatora')
    for i in range(1, n+1):
        print('produkuje', i)
        yield i

    print('koniec generatora')
    # implicit return



def g_3_liczby():
    """Najprostszy generator: trzy kolejne yield."""
    yield 33
    yield 55
    yield 11


if __name__ == "__main__":
    print(1)
    g = f2(10)
    print(g)
    print(2)
    for i in g:
        print('drukuje', i)
        break
    for i in g_3_liczby():
        print(i)
