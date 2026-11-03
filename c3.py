"""
1. open a text file
2. write 2 generator expressions:
   - prepends a line numer to a line
   - prepends current timestamp to a line
3. print all the lines after passing them through these two gen expressions:
"""
import typing

def doklej_timestamp(g: typing.Iterable[str], format='%Y-%m-%d %H:%M:%S'):
    for linia in g:
        yield f'{dt.datetime.now().strftime(format)} {linia}'


def doklej_nr(g, start=0):
    for i, linia in enumerate(g, start=start):
        yield f'{i} {linia}'

import datetime as dt
if __name__ == '__main__':
    with (open('c1.py', 'rt', encoding='utf') as f,
          open('c1.py.out', 'wt', encoding='utf') as f1):
        # timestamp
        # g1 = (f'{dt.datetime.now()} {line}' for line in f)
        g1 = doklej_timestamp(f)
        # line nr
        g2 = doklej_nr(g1)
        # for line in g2:
        #     print(line)
        f1.writelines(g2)

        # druga iteracja:
        # print('drugi raz')
        # for line in g2:
        #     print(line)
