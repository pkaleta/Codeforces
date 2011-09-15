import sys
from math import log

k = int(sys.stdin.readline())
l = int(sys.stdin.readline())

x = int(log(l, k))

if k ** x == l:
    print "YES"
    print x-1
else:
    print "NO"

