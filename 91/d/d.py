import sys

n, k = map(int, sys.stdin.readline().split())
s = list(sys.stdin.readline()[:-1])

for p in xrange(n-1):
    if k == 0:
        break
    if s[p] == '4' and s[p+1] == '7':
        if p % 2 != 0:
            if p >= 1 and s[p-1] == '4':
                if k % 2 != 0:
                    s[p] = '7'
                break
            else:
                s[p] = '7'
        else:
            if p+2 < n and s[p+2] == '7':
                if k % 2 != 0:
                    s[p+1] = '4'
                break
            else:
                s[p+1] = '4'
        k -= 1

print ''.join(s)
