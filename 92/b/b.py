import sys
from itertools import permutations

n, k = map(int, sys.stdin.readline().split())

x = []
for i in xrange(n):
    x.append(sys.stdin.readline().strip())


def permute(n, perm):
    ret = []
    for i in perm:
        ret.append(n[i])
    return int(''.join(ret))

ret = float('inf')
for p in permutations(range(k)):
    xmax = -1
    xmin = float('inf')
    for n in x:
        xmax = max(xmax, permute(n, p))
        xmin = min(xmin, permute(n, p))
    ret = min(ret, xmax-xmin)

print "["
for i in xrange(1, 9):
    perms = []
    for p in permutations(range(i)):
        perms.append(p)
    print perms, ","
print "]"
