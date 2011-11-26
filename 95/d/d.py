import sys

n = int(sys.stdin.readline())
d = [[] for i in xrange(3005)]

for i in xrange(n):
    a, b = map(int, sys.stdin.readline().split())
    d[a].append(b)
    d[b].append(a)

c = []
inC = [False for i in xrange(3005)]

def findCycle():
    stack = [1]
    visited = [False for i in xrange(3005)]
    visited[1] = True
    prev = -1

    while True:
        # print stack
        v = stack[-1]
        finished = True
        for u in d[v]:
            # print "widze", u
            # print "prev", prev
            # if len(stack) >= 2:
            #     print "stack-2", stack[-2]
            if not visited[u]:
                visited[u] = True
                prev = v
                stack.append(u)
                finished = False
                # print "whodze do", u, "ustawiam prev na", v
                break
            elif len(stack) >= 2 and prev != u and u != stack[-2]:
                j = len(stack)-1
                while stack[j] != u:
                    inC[stack[j]] = True
                    c.append(stack[j])
                    j -= 1
                inC[u] = True
                c.append(u)
                return c
        if finished:
            # print "***ustawiam prev na", stack[-1]
            prev = stack[-1]
            stack = stack[:-1]

findCycle()

distance = [0 for i in xrange(3005)]
visited = [False for i in xrange(3005)]

def dfs(v, curDist):
    distance[v] = curDist
    visited[v] = True
    for u in d[v]:
        if not visited[u] and not inC[u]:
            dfs(u, curDist+1)

for v in c:
    dfs(v, 0)

print ' '.join(map(str, distance[1:n+1]))

