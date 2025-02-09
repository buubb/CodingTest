import sys
from collections import defaultdict
input = sys.stdin.readline

class Solution:
    def dist_nodes(self):
        n, m = map(int, input().split())
        tree = defaultdict(list)
        for _ in range(n-1):
            v, k, w = map(int, input().split())
            tree[v].append((k,w))
            tree[k].append((v,w))
            
        find = [tuple(map(int, input().split())) for _ in range(m)]

        def dfs(node, dist, k):
            if node == dist:
                print(k)
                return
            
            for (v,w) in tree[node]:
                if not visited[v]:
                    visited[v] = True
                    dfs(v, dist, k+w)

        for (start, dist) in find:
            visited = [False] * (n+1)
            visited[start] = True
            dfs(start, dist, 0)





if __name__ == "__main__":
    s = Solution()
    s.dist_nodes()