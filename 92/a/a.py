import sys

n, a, b = map(int, sys.stdin.readline().split())

if a+b == n:
    print b
elif a+b > n:
    print n-a
else:
    print b+1
