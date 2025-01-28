import sys
from collections import defaultdict
input = sys.stdin.readline

class Solution:
    find: bool = False
    def family_(self):
        n = int(input())
        a,b = map(int, input().split())
        m = int(input())
        grid = defaultdict(list)
        for _ in range(m):
            parent, child = map(int, input().split())
            grid[parent].append(child)
            grid[child].append(parent)

        visited = [False] * (n+1)
        find = False
        def dfs(node, cnt):
            nonlocal find
            if node == b:
                print(cnt)
                find = True
                return
            
            for i in grid[node]:
                if not visited[i]:
                    visited[i] = True
                    dfs(i, cnt+1)
        
        dfs(a,0)
        if not find:
            print(-1)


if __name__ == "__main__":
    s = Solution()
    s.family_()