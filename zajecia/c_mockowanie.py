"""MagicMock: atrybuty i metody tworzone w locie, return_value, call_count, call_args."""

from unittest.mock import MagicMock

m = MagicMock()
w = m.jakas_metoda()
print(w)
w1 = w.inna_metoda()
print(w1)
m.trzecia_metoda.return_value = 12
w2 = m.trzecia_metoda()
w2 = m.trzecia_metoda(12, 22)
print(w2)
print(m.trzecia_metoda.call_count)
# print(m.trzecia_metoda.assert_called_once())
print(m.trzecia_metoda.call_args)
