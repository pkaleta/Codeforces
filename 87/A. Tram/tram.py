import sys

n = int(sys.stdin.readline())

ret = 0
cur = 0
for i in xrange(n):
    a, b = map(int, sys.stdin.readline().split())
    cur = cur - a + b;
    ret = max(ret, cur)

print ret
