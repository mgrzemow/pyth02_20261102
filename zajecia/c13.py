"""Ćwiczenie: wydanie polecenia systemowego przez subprocess i parsowanie wyniku przez re."""

import re

# os.system wyda polecenie ale nie ma możliwości odczytania stdout
# import os
# os.system('pip freeze')
import subprocess
from pprint import pprint


def wczytaj_pakiety(encoding="utf-8"):
    """Zwraca słownik pakietów z pip freeze: nazwa i wersja rozbita na części."""
    regex1 = r"([\w-]+)==(\d+)\.(\d+)(\.(.+))?\n"
    # pip freeze to tylko przykład: chodzi o odczyt wyjścia polecenia systemowego
    # UWAGA: kodowanie wyjścia zależy od systemu i powłoki, a na Windows często nie jest to utf-8;
    # parametr encoding musi się z nim zgadzać, bo inaczej grozi UnicodeDecodeError albo krzaki
    r = subprocess.run("pip freeze", capture_output=True, shell=True, encoding=encoding)
    wydruk = r.stdout
    wynik = {}
    wrc = re.compile(regex1)
    for m in wrc.finditer(wydruk):
        g = m.groups()
        wynik[g[0]] = (int(g[1]), int(g[2]), g[4])
    return wynik


if __name__ == "__main__":
    pprint(wczytaj_pakiety())
