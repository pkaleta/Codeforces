import sys

a, b, m = map(int, sys.stdin.readline().split())

if b >= m:
    print 2
else:
    found = False
    for i in xrange(1, min(a+1, m)):
        x = (i * 1000000000) % m
        if x != 0 and b < m-x:
            found = True
            print "1 %09d" % i
            break
    if not found:
        print "2"

