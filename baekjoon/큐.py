import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
Q = deque()
for _ in range(N):
    arr=list(input().split())
    if arr[0] == "push":
        Q.append(int(arr[1]))
    elif arr[0] == "pop":
        if not Q:
            print(-1)
        else:
            print(Q.popleft())
    elif arr[0] == "size":
        print(len(Q))
    elif arr[0] == "empty":
        if not Q:
            print(1)
        else:
            print(0)
    elif arr[0] == "front":
        if not Q:
            print(-1)
        else:
            print(Q[0])
    elif arr[0] == "back":
        if not Q:
            print(-1)
        else:
            print(Q[-1])
