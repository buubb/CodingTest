import sys
from collections import defaultdict
input = sys.stdin.readline

class Solution:
    def find(self, k, parent):
        if parent[k] != k:
            parent[k] = self.find(parent[k], parent)
        return parent[k]
    
    def union(self, a, b, parent, grid):
        r1 = self.find(a, parent)
        r2 = self.find(b, parent)

        if r1 != r2:
            if r1 < r2:
                parent[r2] = r1
                grid[r1] = (
                    max(grid[r1][0], grid[r2][0]),
                    min(grid[r1][1], grid[r2][1]),
                    max(grid[r1][2], grid[r2][2]),
                    min(grid[r1][3], grid[r2][3])
                )
            else:
                parent[r1] = r2
                grid[r2] = (
                    max(grid[r1][0], grid[r2][0]),
                    min(grid[r1][1], grid[r2][1]),
                    max(grid[r1][2], grid[r2][2]),
                    min(grid[r1][3], grid[r2][3])
                )
    
    def answer(self):
        n,m = map(int, input().split())
        parent = list(range(n+1))
        grid = {}
        
        for i in range(1, n+1):
            x, y = map(int, input().split())
            grid[i] = (x, x, y, y)
       
        for _ in range(m):
            a,b = map(int, input().split())
            self.union(a,b,parent,grid)
        
        res = float('inf')
        check = set(self.find(i, parent) for i in range(1, n+1))
        for i in check:
            a = grid[i][0] - grid[i][1]
            b = grid[i][2] - grid[i][3]

            res = min(res, 2*(a+b))
        print(res)
if __name__ == "__main__":
    s = Solution()
    s.answer()