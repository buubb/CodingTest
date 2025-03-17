import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def answer(self):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            grid.append(list(input().strip()))

        res = float('inf')
        for i in range(n-7):
            for j in range(m-7):
                w, b = 0, 0
                for x in range(i, i+8):
                    for y in range(j, j+8):
                        if (x+y) % 2 == 0:
                            if grid[x][y] != 'W':
                                w += 1
                            else:
                                b += 1
                        else:
                            if grid[x][y] != 'B':
                                w += 1
                            else:
                                b += 1
                res = min(res, w, b)
        print(res)

                        
                    


if __name__ == "__main__":
    s = Solution()
    s.answer()