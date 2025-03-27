import sys
from collections import deque
input = sys.stdin.readline # sys.stdin.readline을 사용하지 않으면 시간초과

class Solution:
    def answer(self):
        n = int(input())
        Q = deque()
        for _ in range(n):
            oper = list(input().split())

            if oper[0] == "push":
                Q.append(oper[1])
            elif oper[0] == "pop":
                print(-1 if not Q else Q.popleft())
            elif oper[0] == "size":
                print(len(Q))
            elif oper[0] == "empty":
                print(1 if not Q else 0)
            elif oper[0] == "front":
                print(-1 if not Q else Q[0])
            elif oper[0] == "back":
                print(-1 if not Q else Q[-1])


if __name__ == "__main__":
    s = Solution()
    s.answer()