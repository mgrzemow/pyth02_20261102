# napisać dekokator logujący wywołania dekorowanej funkcji
import functools
import logging

logging.basicConfig(level=logging.DEBUG, filename='log.txt', filemode='w', encoding='utf-8')

# za pierwszym razem tworzymy obiekt loggera
logger = logging.getLogger(__name__)
# a tu już zwracany ze slownika, więc to jest tanie
logger = logging.getLogger(__name__)
logger = logging.getLogger(__name__)

# ważne - loggery dziedziczą ustawienia na podstaie swoich nazw
# jeżeli stworzę logger o id: l1
l1 = logging.getLogger('l1')
# powiedzmy że to dodatkowo konfigurujemy ten logger
# to logger o id l1.l2 dostanie jego ustawienia
l2 = logging.getLogger('l1.l2')

l1.log(logging.DEBUG, 'test')

class loguj_wywolania:
    def __init__(self, ok_level=logging.DEBUG, error_level=logging.ERROR):
        ...
    def __call__(self, f_dekorowana):
        @functools.wraps(f_dekorowana)
        def nowa_funkcja(*args, **kwargs):
            print('nowa_funkcja przed wywolaniem oryginalnej', args, kwargs, self.p1)
            r = f_dekorowana(*args, **kwargs)
            print('nowa_funkcja po wywolaniu oryginalnej', args, kwargs, r)
            return r
        return nowa_funkcja

@loguj_wywolania()
def f1(x, y):
    return x / y

if __name__ == '__main__':
    f1(1, 2)
    f1(1, 0)
