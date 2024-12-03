from collections import deque
import sys
N = int(sys.stdin.readline())

Q = deque()

for _ in range(N):
    a = list(sys.stdin.readline().split())
    if a[0] == "push_back":
        Q.append(a[1])
    elif a[0] == "push_front":
        Q.appendleft(a[1])
    elif a[0] == "front":
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[0])
    elif a[0] == "back":
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[-1])
    elif a[0] == "pop_front":
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.popleft())
    elif a[0] == "pop_back":
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.pop())
    elif a[0] == "size":
        print(len(Q))
    elif a[0] == "empty":
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    
