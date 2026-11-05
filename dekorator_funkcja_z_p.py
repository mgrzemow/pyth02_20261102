import functools

def dekorator(p1=None):
    def dekorator_wlasciwy(f_dekorowana):
        @functools.wraps(f_dekorowana)
        def nowa_funkcja(*args, **kwargs):
            print('nowa_funkcja przed wywolaniem oryginalnej', args, kwargs, p1)
            r = f_dekorowana(*args, **kwargs)
            print('nowa_funkcja po wywolaniu oryginalnej', args, kwargs, r)
            return r
        return nowa_funkcja
    return dekorator_wlasciwy

@dekorator(p1=12)
def f(x):
    print('f', x)
    return 55

print(f(1))