"""Ćwiczenie: numeracja i znacznik czasu dla linii pliku przez wyrażenia generatorowe.

1. open a text file
2. write 2 generator expressions:
   - prepends a line numer to a line
   - prepends current timestamp to a line
3. print all the lines after passing them through these two gen expressions:
"""

import datetime as dt
from pathlib import Path

if __name__ == "__main__":
    with open(Path(__file__).with_name("c1.py"), "rt", encoding="utf") as f:
        # timestamp
        g1 = (f"{dt.datetime.now()} {line}" for line in f)
        # line nr
        g2 = (f"{i} {line}" for i, line in enumerate(g1))

        for line in g2:
            print(line)
        # druga iteracja:
        # print('drugi raz')
        # for line in g2:
        #     print(line)
