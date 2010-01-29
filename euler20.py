#!/usr/bin/python
from utils import facto

f = facto(100)
print f

r = str(f)
print len(r)

s = 0
for i in range(len(r)):
    s += int(r[i])

print s

# Another intersting solution
# reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))])
