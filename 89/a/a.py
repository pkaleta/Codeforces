import sys

s = sys.stdin.readline()[:-1]

ret = []
for c in s:
    if not c.upper() in ["A", "O", "Y", "E", "U", "I"]:
        ret.append('.')
        if c.isupper():
            ret.append(c.lower())
        else:
            ret.append(c)

print ''.join(ret)
