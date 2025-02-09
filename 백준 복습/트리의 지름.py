import sys
from collections import defaultdict, deque
input = sys.stdin.readline

class Solution:
    def tree_radius(self):
        n = int(input())
        tree = defaultdict(list)
        for _ in range(n-1):
            x, y, w = map(int, input().split())
            tree[x].append((y,w))
            tree[y].append((x,w))

        def bfs(node):
            Q = deque()
            Q.append((node, 0))
            visited = [False] * (n+1)
            max_value = (0,node)
            while Q:
                v, w = Q.popleft()
                max_value = max(max_value, (w, v))
                for (dv, dw) in tree[v]:
                    if not visited[dv]:
                        Q.append((dv, w + dw))
                        visited[dv] = True
            return max_value

        _, first_node = bfs(1)
        res, _ = bfs(first_node)
        print(res)
        
if __name__ == "__main__":
    s = Solution()
    s.tree_radius()