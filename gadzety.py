# imie = input('Podaj imie:')
# while imie != 'stop':
#     print(imie)
#     imie = input('Podaj imie:')

# imie = None
# while imie != 'stop':
#     if imie is not None:
#         print(imie)
#     imie = input('Podaj imie:')

# while True:
#     imie = input('Podaj imie:')
#     if imie == 'stop':
#         break
#     print(imie)

# from 3.8 :=
# while (imie := input('Podaj imie:')) != 'stop':
#     print(imie)

# inne użycie
h = 10
r = 10
v = (s := 3.14 * r * r) * h
print(s, v)

# opearatory slownikowe | |=, new in 3.14
d1 = {1:11, 2:22, 3:33}
d2 = {3:333, 4:444}

print({**d1, **d2})
print(d1 | d2)
d1 |= d2
print(d1)
