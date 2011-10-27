import sys

n = int(sys.stdin.readline())

def check(n):
    for d in str(n):
        if d != '4' and d != '7':
            return False
    return True

for i in xrange(4, n+1):
    if n % i == 0 and check(i):
        print 'YES'
        exit(0)

print 'NO'
