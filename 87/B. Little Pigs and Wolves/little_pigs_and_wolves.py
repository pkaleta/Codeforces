import sys

n, m = map(int, sys.stdin.readline().split())
g = []


def count(i, j):
    if g[i][j] == 'P':
        return (g[i-1][j] == 'W') + (g[i+1][j] == 'W') + (g[i][j-1] == 'W') + (g[i][j+1] == 'W')
    else:
        return 0

g.append(['.' for i in xrange(m+4)])
g.append(['.' for i in xrange(m+4)])
for i in xrange(1, n+1):
    l = ['.', '.']
    l += list(sys.stdin.readline()[:-1])
    l += ['.', '.']
    g.append(l)
g.append(['.' for i in xrange(m+4)])
g.append(['.' for i in xrange(m+4)])

#for i in g:
#    print i

ret = 0
for i in xrange(2, n+2):
    for j in xrange(2, m+2):
        if g[i][j] == 'W':
#            print 'jestem', i, j
            l = [(count(i-1, j), i-1, j), (count(i+1, j), i+1, j), (count(i,j-1), i, j-1), (count(i, j+1), i, j+1)]
            l = filter(lambda (a, b, c): a > 0, l)
            l = sorted(l, key=lambda (a, b, c): a)
#            print l
            if len(l) > 0:
                (_, y, x) = l[0]
                ret += 1
                g[y][x] = '.'

print ret



