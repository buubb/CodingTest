import sys
from collections import defaultdict, deque
input = sys.stdin.readline

class Solution:
    def dist_between_nodes(self):
        N, M = map(int, input().split())
        graph = defaultdict(list)
        for _ in range(N-1):
            a,b,w = map(int, input().split())
            graph[a].append((b,w))
            graph[b].append((a,w))
        
        
        def bfs(node, target):
            Q = deque()
            Q.append((node, 0))
            visited = [False] * (N+1)
            visited[node] = True
            while Q:
                n, w = Q.popleft()
                if n == target:
                    return w
                for i, dw in graph[n]:
                    if not visited[i]:
                        Q.append((i, w+dw))
                        visited[i] = True
            return -1
                

        for _ in range(M):
            x, y = map(int, input().split())
            print(bfs(x,y))

if __name__ == "__main__":
     s = Solution()
     s.dist_between_nodes()
