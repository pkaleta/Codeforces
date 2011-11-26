import sys

w = sys.stdin.readline().strip()

count = 0
for i in xrange(1, len(w)):
    if w[i] >= 'A' and w[i] <= 'Z':
        count += 1

if count == len(w)-1:
    if w[0] >= 'A' and w[0] <= 'Z':
        print w.lower()
    else:
        print w[0].upper() + w[1:].lower()
else:
    print w
