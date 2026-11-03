def f1(n):
    y = []
    for i in range(n):
        print('produkuje', i)
        y.append(i)
    return y

def f2(n):
    print('start generatora')
    for i in range(1, n+1):
        print('produkuje', i)
        yield i

    print('koniec generatora')
    # implicit return

print(1)
g = f2(10)
print(g)
print(2)

for i in g:
    print('drukuje', i)
    break

def g_3_liczby():
    yield 33
    yield 55
    yield 11

for i in g_3_liczby():
    print(i)