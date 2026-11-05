"""Importuje p1.m1, żeby pokazać wartość __name__ w module importowanym."""

import p1.m1  # wypisuje p1.m1

if __name__ == "__main__":
    print("moduł p1.m1:", p1.m1.__name__)
