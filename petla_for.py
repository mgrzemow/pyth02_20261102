x = [1, 2, 3, 4]

for e in x:
    print(e)

# side note - most of global functions delegate calls to methods
# if we have a function aaa(object), then it will call object.__aaa__()

# it = iter(x)
it = x.__iter__()
print(it)
# print(next(it))
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
# print(it.__next__())

print('asdasd'.__iter__())
print({1:11, 2:22}.__iter__())

with open('c1.py', 'rt', encoding='utf') as f:
    for line in f:
        print(line)

# how to devepot magic object which are iterable and calculate
# results on the fly
# 1. generator expressions
# 2. functions with yield
# 3. classes with __iter__ and __next__
