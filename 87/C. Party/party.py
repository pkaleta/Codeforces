import sys

n = int(sys.stdin.readline())

parent = {}

for i in xrange(1, n+1):
    p = int(sys.stdin.readline())
    parent[i] = p

ret = 0
for i in xrange(1, n+1):
    cur = 1
    j = i;
    while parent[j] != -1:
        cur += 1
        j = parent[j]
    ret = max(ret, cur)

print ret

