import sys
from copy import copy

n, k = map(int, sys.stdin.readline().split())
tmp = list(map(int, sys.stdin.readline()[:-1]))

s = []
for i in xrange(len(tmp)):
    s.append((tmp[i], i))

cur = -1
def comp((a, ap), (b, bp)):
    global cur
    x = abs(a-cur)
    y = abs(b-cur)
    if x != y:
        return x-y
    else:
        if bp > ap:
            return -1
        else:
            return 1

def tostr(x):
    return ''.join(map(str, x))

def repl(d, new):
    global tmp
    x = copy(tmp)
    for (_, pos) in d:
        x[pos] = new
    return x

mincost = float('inf')
d = []
new = -1
ret = ''.join(['9']*100000)
for i in xrange(0, 10):
    cur = i
    sort = sorted(s, cmp=lambda (a, ap), (b, bp): abs(a-i)-abs(b-i))

    cost = 0
    for j in xrange(k):
        cost += abs(sort[j][0]-i)
#    print i, sort, cost

    if cost < mincost:
        mincost = cost
        d = sort[:k]
        ret = tostr(repl(d, i))
    elif cost == mincost:
        mincost = cost
        d = sort[:k]
        rpl = repl(d, i)
        if tostr(rpl) < tostr(ret):
            ret = tostr(rpl)

print mincost
print ret

