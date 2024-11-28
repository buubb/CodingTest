import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
res = []
pr = [0] * N
for i, tower in enumerate(arr):
    while res and res[-1][1] <= tower:
        res.pop()
    if res:
        pr[i] = res[-1][0]
    res.append((i+1, tower))
   
print(*pr)