import sys
from collections import deque
input = sys.stdin.readline
class Solution:
    def startlink(self):
        F, S, G, U, D = map(int, input().split())
        
        def bfs():
            Q = deque()
            Q.append((S, 0))
            visited = set()
            visited.add(S)
            while Q:
                floor, count = Q.popleft()
                if floor == G:
                    return count
                plus = floor + U
                minus = floor - D
                if plus <= F and plus not in visited:
                    Q.append((plus, count+1))
                    visited.add(plus)
                if minus >= 1 and minus not in visited:
                    Q.append((minus, count+1))
                    visited.add(minus)
            return -1
        res = bfs()
        if res != -1:
            print(res)
        else:
            print("use the stairs")

if __name__ == "__main__":
    s = Solution()
    s.startlink()