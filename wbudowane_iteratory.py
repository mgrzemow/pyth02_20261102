x = ['ala', 'tomek', 'zosia']
print(list(enumerate(x)))
for i, line in enumerate(x):
    print(i, line)

# zip
print(zip([1,2,3], [11,22,33]))
print(list(zip([1,2,3], [11,22,33])))

{}.items()
{}.keys()
{}.values()

# reversed()

# range()

import itertools
x1 = [1,2,3]
x2 = [4,5,6]
for i in itertools.chain(x1, x2):
    print(i)

for i in itertools.batched('abcdefghij', n=3):
    print(i)

for i in itertools.pairwise('abcdefghij'):
    print(i)

x = ['ala', 'tomek', 'zosia', 'karol', 'marysia']
y = ['raz', 'dwa']
for i in zip(x, itertools.cycle(y)):
    print(i)

x = ['ala', 'tomek', 'zosia', 'karol', 'marysia']
y = ['raz', 'dwa']
for i, j in zip(x, y):
    print(i, j)

x = ['ala', 'tomek', 'zosia', 'karol', 'marysia']
y = ['raz', 'dwa']
for i, j in itertools.zip_longest(x, y, fillvalue='ciociamarysia'):
    print(i, j)

# if you need more generic iterators:
# https://more-itertools.readthedocs.io/en/stable/
