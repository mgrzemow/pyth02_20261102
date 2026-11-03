"""
1. open a text file
2. write 2 generator expressions:
   - prepends a line numer to a line
   - prepends current timestamp to a line
3. print all the lines after passing them through these two gen expressions:
"""

if __name__ == '__main__':
    with open():
        # timestamp
        g1 = (...)
        # line nr
        g2 = (...)
        for line in g2:
            print(line)
