import sys

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227, 229]

n = int(sys.stdin.readline())

if n == 2:
    print -1
else:
    tmp = 1
    for i in xrange(n):
        tmp *= primes[i]

    for i in xrange(n):
        print tmp / primes[i]
