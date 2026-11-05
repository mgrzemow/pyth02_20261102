# napisać dekorator, który
# próbuje skonwertować wartość zwracaną do int
# jak się nie uda to próbuje do float
# jak się nie uda do float to się wywala z ValueError
import functools


def value_error_to_none(f_dekorowana):
    @functools.wraps(f_dekorowana)
    def nowa_funkcja(*args, **kwargs):
        # przed
        try:
            return f_dekorowana(*args, **kwargs)
        except ValueError:
            return None
    return nowa_funkcja

# można ale obstawiam że to brzydko wybuchnie
int = value_error_to_none(int)

if __name__ == '__main__':
    print(int('aka'))
    x = 12
    y = 44
    print(x + y)