"""Pokazuje wartość __name__: p1.m1 przy imporcie, __main__ przy uruchomieniu."""

print(__name__)  # celowo poza blokiem __main__, żeby wykonało się także przy imporcie

if __name__ == "__main__":
    print('uruchomiono moduł bezpośrednio')
