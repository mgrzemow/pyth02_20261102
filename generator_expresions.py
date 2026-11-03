x = range(10_000_000)
input('stop')
y1 = (i / 13 for i in x)
print(y1)
input('stop')
y2 = (i * 4 for i in y1)
print(y2)
input('stop')
# for i in y2:
#     if i > 1000:
#         break
#     print(i)

# naming:
# iterable - whatever will work in for loop
# generator - function with yield
# iterator - everything else

# sometimes iterator will be separate from the iterable
x = [1,2,3,4]
it = x.__iter__()
print(it is x)

#sometimes it will the the same object
g = (i**2 for i in range(10))
it = g.__iter__()
print(g is it)
