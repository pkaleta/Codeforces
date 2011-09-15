import sys

n, m = map(int, sys.stdin.readline().split())
names = []
pairs = []

for i in xrange(n):
    name = sys.stdin.readline()[:-1]
    names.append(name)

for i in xrange(m):
    a, b = sys.stdin.readline()[:-1].split()
    pairs.append((a, b))

def check(cur):
    for (a, b) in pairs:
        if a in cur and b in cur:
            return False
    return True

r = 2**n
maxNames = []

for i in xrange(r):
    n = i
    cur = []
    j = 0
#    print n
    while n > 0:
        if n % 2 == 1:
            cur.append(names[j])
        n /= 2
        j += 1
    if check(cur) and len(cur) > len(maxNames):
        maxNames = []
        for k in xrange(len(cur)):
            maxNames.append(cur[k])

print len(maxNames)
print '\n'.join(sorted(maxNames))

