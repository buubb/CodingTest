import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class Solution:
    def cebu(self):
        n, m = map(int, input().split())
        s, e = map(int, input().split())
        graph = defaultdict(list)
        
        for _ in range(m):
            v1, v2, w = map(int, input().split())
            graph[v1].append((w, v2))
            graph[v2].append((w, v1))
        
        visited = [False] * (n+1)
        res = 0
        def dfs(v, tmp, visited):
            nonlocal res
            if v == e:
                res = max(res, min(tmp))
                return
            
            for dw, dv in sorted(graph[v], reverse=True):  
                if not visited[dv]:
                    tmp.append(dw)
                    visited[dv] = True
                    dfs(dv, tmp, visited)
                    visited[dv] = False
                    tmp.pop()
        
        visited[s] = True
        dfs(s, [], visited)
        print(res)

if __name__ == "__main__":
    s = Solution()
    s.cebu()