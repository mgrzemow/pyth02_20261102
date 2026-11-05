"""Ćwiczenie: odczyt pip freeze przez subprocess i parsowanie wyrażeniem regularnym."""
import re

# os.system wyda polecenie ale nie ma możliwości odczytania stdout
# import os
# os.system('pip freeze')
import subprocess
from pprint import pprint


def wczytaj_pakiety(encoding='utf-8'):
    """Zwraca słownik pakietów z pip freeze: nazwa i wersja rozbita na części."""
    regex1 = r'([\w-]+)==(\d+)\.(\d+)(\.(.+))?\n'
    r = subprocess.run('pip freeze', capture_output=True, shell=True, encoding=encoding)
    wydruk = r.stdout
    wynik = {}
    wrc = re.compile(regex1)
    for m in wrc.finditer(wydruk):
        g = m.groups()
        wynik[g[0]] = (int(g[1]), int(g[2]), g[4])
    return wynik


if __name__ == '__main__':
    pprint(wczytaj_pakiety())
