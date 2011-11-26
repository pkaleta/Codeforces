import sys

n = sys.stdin.readline()
t = map(int, sys.stdin.readline().split())

count = {}
for i in xrange(-10, 11):
    count[i] = 0;

ret = 0
for x in t:
    count[x] += 1

for x in t:
    ret += count[-x]
    if x == 0:
        ret -= 1

print ret / 2


