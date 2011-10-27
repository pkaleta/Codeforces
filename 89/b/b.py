import sys

n = int(sys.stdin.readline())

def line(x):
    line = [' ']*(n-x)
    for i in xrange(x+1):
        line.append(str(i))
    for i in xrange(x-1, -1, -1):
        line.append(str(i))
    return ' '.join(line)

for i in xrange(n+1):
    print line(i)

for i in xrange(n-1, -1, -1):
    print line(i)


