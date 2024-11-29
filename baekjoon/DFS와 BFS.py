from sys import stdin
from collections import deque, defaultdict

class Solution:
    def dfsAndBfs(self):
        N, M, V = map(int, stdin.readline().split())
        graph = defaultdict(list)
        for i in range(M):
            a, b = map(int, stdin.readline().split())
            graph[a].append(b)
            graph[b].append(a)
            
        d = []
        visited_d = set()
        def dfs(node):
            d.append(node)
            visited_d.add(node)
            for v in sorted(graph[node]):
                if v not in visited_d:
                    dfs(v)
        
        def bfs(node):
            Q = deque()
            Q.append(node)
            res = []
            visited = set()
            
            while Q:
                v = Q.popleft()
                for i in sorted(graph[v]):
                    if i not in visited:
                        Q.append(i)
                if v not in visited:
                    res.append(v)
                    visited.add(v)
                
            return res


        dfs(V)
        print(*d)
        print(*bfs(V))



if __name__ == "__main__":
    s = Solution()
    s.dfsAndBfs()