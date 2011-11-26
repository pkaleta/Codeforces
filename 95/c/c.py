import sys

dp = [[-1 for i in xrange(50)] for j in xrange(50)]

def bc(n, k):
    if k == 0:
        return 1
    if n == 0:
        return 0
    if dp[n][k] != -1:
        return dp[n][k]

    dp[n][k] = bc(n-1, k-1) + bc(n-1, k)
    return dp[n][k]

n, m, t = map(int, sys.stdin.readline().split())

ret = 0
for i in xrange(4, n+1):
    for j in xrange(1, m+1):
        if i+j == t:
            ret += bc(n, i) * bc(m, j)

print ret
