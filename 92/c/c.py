import sys

MAX_N = 1005

s = ' ' + sys.stdin.readline().strip()

primes = []

isPrime = [True for i in xrange(MAX_N)]
isPrime[0] = False
isPrime[1] = False

for i in xrange(2, MAX_N):
    if isPrime[i]:
        primes.append(i)
        x = 2 * i
        while x < MAX_N:
            isPrime[x] = False
            x += i

assigned = [-1 for i in xrange(MAX_N)]
count = [0 for i in xrange(MAX_N)]
count2 = {}

maxCount = 0
for c in s:
    if count2.has_key(c):
        count2[c] += 1
    else:
        count2[c] = 1
    maxCount = max(count2[c], maxCount)

cur = 0
for i in xrange(1, len(s)):
    if isPrime[i]:
#        print i
        x = i
        found = -1
        while x < len(s):
            if assigned[x] != -1:
                found = assigned[x]
                break
            x += i

#        print "****", found
        toSet = None
        if found == -1:
            toSet = cur
            cur += 1
        else:
            toSet = found

        x = i
        while x < len(s):
#            print x, toSet
            if assigned[x] == -1:
                count[toSet] += 1
            assigned[x] = toSet
            x += i


if maxCount < count[0]:
    print "NO"
else:
    count2.pop(' ')
    count2 = sorted(count2.items(), key=lambda x: x[1])[::-1]
#   print count2
    c, cnt = count2[0]
    count2[0] = (c, cnt-count[0])
    ret = [' ' for i in xrange(len(s))]
    for i in xrange(len(s)):
        if assigned[i] == 0:
            ret[i] = c
    count2 = map(list, count2)
#    print count2, ret

    cur = 0
    if count2[cur][1] == 0:
        cur += 1
    i = 0
    for i in xrange(1,len(s)):
        if ret[i] == ' ':
            ret[i] = count2[cur][0]
            count2[cur][1] -= 1
            if count2[cur][1] == 0:
                cur += 1

    print "YES"
    print ''.join(ret[1:])

# print assigned[1:10]
# print count[:50]

