import sys
from collections import defaultdict, deque
input = sys.stdin.readline

class Solution:
    def dfs_bfs(self):
        n,m,v = map(int, input().split())
        graph = defaultdict(list)
        for _ in range(m):
            a,b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
        d = []
        visited = [False] * (n+1)
        def dfs(node):
            if visited[node]:
                return
            d.append(node)
            visited[node] = True
            for v in sorted(graph[node]):
                if not visited[v]:
                    dfs(v)

        b = []
        def bfs(node):
            Q = deque()
            Q.append(node)
            visits = [False]*(n+1)
            visits[node] = True
            while Q:
                v = Q.popleft()
                b.append(v)
                for nv in sorted(graph[v]):
                    if not visits[nv]:
                        Q.append(nv)
                        visits[nv] = True
        
        dfs(v)
        bfs(v)
        print(*d)
        print(*b)

if __name__ == "__main__":
    s = Solution()
    s.dfs_bfs()