import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class Solution:
    # 시간 초과과
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

    def find(self, k, parent):
        if parent[k] != k:
            parent[k] = self.find(parent[k], parent)
        return parent[k]
    
    def union(self, a, b, parent):
        r1 = self.find(a, parent)
        r2 = self.find(b, parent)

        if r1 < r2:
            parent[r2] = r1
        elif r1 > r2:
            parent[r1] = r2

    def cebu2(self):
        n, m = map(int, input().split())
        s, e = map(int, input().split())
        
        edges = []
        for _ in range(m):
            v1, v2, w = map(int, input().split())
            edges.append((w, v1, v2))
        
        edges.sort(reverse=True)
        
        parent = [i for i in range(n+1)]

        for cost, a, b in edges:
            self.union(a, b, parent)
            if self.find(s, parent) == self.find(e, parent):
                print(cost)
                return
        
        print(0)

        

if __name__ == "__main__":
    s = Solution()
    s.cebu2()