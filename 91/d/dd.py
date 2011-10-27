import sys

n, k = map(int, sys.stdin.readline().split())
s = [' '] + list(sys.stdin.readline()[:-1])

pos = []

# for i in xrange(len(s)-1):
#     if s[i:i+2] == '47':
#         pos.append(i)

p = 0
while k > 0 and p < len(s)-1:
    if s[p] == '4' and s[p+1] == '7':
#        print p, p+1
        if p % 2 == 0:
            if p >= 1 and s[p-1] == '4':
                if k % 2 != 0:
                    s[p] = '7'
                break
            else:
                s[p] = '7'
        else:
            if p+2 < len(s) and s[p+2] == '7':
                if k % 2 != 0:
                    s[p+1] = '4'
                break
            else:
                s[p+1] = '4'
        k -= 1
    p += 1


print ''.join(s[1:])
