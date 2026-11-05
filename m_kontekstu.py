"""Menedżer kontekstu: __exit__ wywołuje się także przy wyjątku."""


# python guarantees __exit__
# use instead of destructor
class MyContextManager:
    """Menedżer kontekstu wypisujący informacje o wyjątku."""

    def __enter__(self):
        """Zwraca obiekt przypisywany przez as."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Wypisuje dane wyjątku; zwrócenie True by go wyciszyło."""
        print("exit", exc_type, exc_value, traceback)
        # if __exit__returns True, it will block the exception
        # return True


if __name__ == "__main__":
    x = MyContextManager()
    # __exit__ dostaje wyjątek, a ten leci dalej, bo __exit__ nie zwraca True
    try:
        with x as alias:
            print(x, alias)
            9 / 0
    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)

    print("after exit")
