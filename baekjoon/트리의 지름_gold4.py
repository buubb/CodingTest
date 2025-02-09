import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
class Solution:
    def tree_radius(self):
        n = int(input())
        tree = defaultdict(list)
        for _ in range(n-1):
            par, chi, w = map(int, input().split())
            tree[par].append((chi, w))
            tree[chi].append((par, w))

        def dfs(node, visited, dist):
            visited[node] = True
            farthest_node = node
            max_dist = dist

            for v, w in tree[node]:
                if not visited[v]:
                    far_node, far_dist = dfs(v, visited, dist+w)
                    if far_dist > max_dist:
                        farthest_node = far_node
                        max_dist = far_dist
            
            return farthest_node, max_dist
        
        # 임의의 노드 1에서 가장 먼 노드 찾기
        visited = [False] * (n+1)
        far_node, _ = dfs(1, visited, 0)

        # 가장 먼 노드에서 먼 노드까지의 길이
        visited = [False] * (n+1)
        _, max_dist = dfs(far_node, visited, 0)

        print(max_dist)


if __name__ == "__main__":
    s = Solution()
    s.tree_radius()