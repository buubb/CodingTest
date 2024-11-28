import sys
from collections import deque
N = int(sys.stdin.readline())
stack = []
mid = []
res = deque()
ss = []
for i in range(N):
    res.append(int(sys.stdin.readline()))
    stack.append(N-i)
prev = 0
while res:
    n = res.popleft()
    if n > prev:
        for i in range(prev, n):
            mid.append(stack.pop())
            prev += 1
            ss.append("+")
        
        mid.pop()
        ss.append("-")
    else:
        if mid and n == mid[-1]:
            mid.pop()
            ss.append("-")

if mid:
    print("NO")
else:
    for i in ss:
        print(i)
