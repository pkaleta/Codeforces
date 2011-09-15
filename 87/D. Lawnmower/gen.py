from random import randint

n = 150
m = 150
print n, m
d = {}

for i in xrange(n):
    l = []
    for j in xrange(m):
        x = randint(0, 100)
        if x == 5:
            d[(i, j)] = True

print d.keys()

