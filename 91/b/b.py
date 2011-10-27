import sys

s = sys.stdin.readline()[:-1]

ret = -1
d = {}

def check(s):
    for c in s:
        if c != '4' and c != '7':
            return False
    return True

maxTimes = -1
for i in xrange(len(s)+1):
    for j in xrange(i+1, len(s)+1):
        sub = s[i:j]
        if check(sub):
            if d.has_key(sub):
                d[sub] += 1
            else:
                d[sub] = 1
            maxTimes = max(maxTimes, d[sub])


if maxTimes == -1:
    print -1
else:
    ret = len(s)*'9'
    for (k, v) in d.items():
        if v == maxTimes and k < ret:
            ret = k

    print ret

