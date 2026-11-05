import functools

class dekorator:
    def __init__(self, p1):
        self.p1 = p1

    def __call__(self, f_dekorowana):
        @functools.wraps(f_dekorowana)
        def nowa_funkcja(*args, **kwargs):
            print('nowa_funkcja przed wywolaniem oryginalnej', args, kwargs, self.p1)
            r = f_dekorowana(*args, **kwargs)
            print('nowa_funkcja po wywolaniu oryginalnej', args, kwargs, r)
            return r
        return nowa_funkcja

@dekorator()
def f(x):
    print('f', x)
    return 55

print(f(1))