import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def stone_game(self):
        N = int(input())

        Q = deque()
        Q.append((N-1, 1))
        Q.append((N-3, 1))
        visited = set()
        visited.add(N-1)
        visited.add(N-3)
        num = step = 0
        while Q:
            num, step = Q.popleft()
            if num == 0:
                if step % 2 != 0:
                    print("SK")
                    return
                else:
                    print("CY")
                    return
            if num >= 1 and num-1 not in visited:
                Q.append((num-1, step+1))
                visited.add(num-1)
            if num >= 3 and num-3 not in visited:
                Q.append((num-3, step+1))
                visited.add(num-3)
        
        
if __name__ == "__main__":
    s = Solution()
    s.stone_game()