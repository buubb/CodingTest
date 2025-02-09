import sys
from collections import defaultdict, deque
input = sys.stdin.readline

class Solution:
    def tree_radius(self):
        n = int(input())
        tree = defaultdict(set)
        for _ in range(n):
            arr = list(map(int, input().split()))
            for i in range(1, len(arr)-2, 2):
                tree[arr[0]].add((arr[i], arr[i+1])) # v, w
                tree[arr[i]].add((arr[0], arr[i+1]))
        
        def bfs(node):
            Q = deque()
            Q.append((node, 0))
            visited = [False] * (n+1)
            visited[node] = True
            max_value = (0, node) # value, node
            while Q:
                v, w = Q.popleft()
                max_value = max(max_value, (w, v))

                for (dv, dw) in tree[v]:
                    if not visited[dv]:
                        Q.append((dv, w+dw))
                        visited[dv] = True
            
            return max_value

        _, node = bfs(1)
        res, _ = bfs(node)

        print(res)

if __name__ == "__main__":
    s = Solution()
    s.tree_radius()