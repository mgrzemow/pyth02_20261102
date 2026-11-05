import functools

# tej wersji nie używamy - zamiast tego zwykła funkcja!!!
# da się naprawić ale po co?

class dekorator:
    def __init__(self, f):
        self.f_dekorowana = f

    def __call__(self, *args, **kwargs):
        print('nowa_funkcja przed wywolaniem oryginalnej', args, kwargs)
        r = self.f_dekorowana(*args, **kwargs)
        print('nowa_funkcja po wywolaniu oryginalnej', args, kwargs, r)
        return r

    def __get__(self, instance, owner):
        return functools.partial(self, instance)

class A:
    @dekorator
    def m1(self, x):
        print('m1', x)
        return 55

a = A()
print(a.m1(1))