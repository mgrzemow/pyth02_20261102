import functools

def dekorator(f_dekorowana):
    @functools.wraps(f_dekorowana)
    def nowa_funkcja(*args, **kwargs):
        print('nowa_funkcja przed wywolaniem oryginalnej', args, kwargs)
        r = f_dekorowana(*args, **kwargs)
        print('nowa_funkcja po wywolaniu oryginalnej', args, kwargs, r)
        return r
    return nowa_funkcja

@dekorator
def f(x):
    print('f', x)
    return 55

import builtins
builtins.len = dekorator(len)
print(len('abc'))

# f = moja_funkcja(f)
# print(f)
# print(f(12))
