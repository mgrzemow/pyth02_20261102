import timeit
def policz_petla():
    y = []
    for i in range(100_000):
        y.append(i**2)
    return y

def policz_comprehension():
    y = [i**2 for i in range(100_000)]
    return y

print(timeit.timeit('policz_petla()', globals=globals(), number=1000))
print(timeit.timeit('policz_comprehension()', globals=globals(), number=1000))

