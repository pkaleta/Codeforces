import sys

n, m = map(int, sys.stdin.readline().split())
g = []

def find(line):
    fst = 200
    lst = -1
    i = 0
    while i < len(line):
        if line[i] == 'W':
            if fst == 200:
                fst = i
            lst = i
        i += 1
#    print (line, fst, lst)
    return (fst, lst)

fst = [200 for i in xrange(200)]
lst = [-1 for i in xrange(200)]
last = 0
for i in xrange(n):
    line = list(sys.stdin.readline()[:-1])
    (f, l) = find(line)
    if f != 200:
        last = i
    g.append(line)
    fst[i] = f
    lst[i] = l

ret = 0
x = 0
for i in xrange(min(n-1, last)):
#    print x
    if i % 2 == 0:
        xx = max([x, lst[i], lst[i+1]])
        ret += xx-x+1
        x = xx
    else:
        xx = min([x, fst[i], fst[i+1]])
        ret += x-xx+1
        x = xx

#print x

if last % 2 == 0:
    xx = max([x, lst[last]])
    ret += xx-x
else:
    xx = min([x, fst[last]])
    ret += x-xx

print ret


