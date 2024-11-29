from sys import stdin
from collections import defaultdict, deque
class Solution:
    def virus(self):
        V = int(stdin.readline())
        K = int(stdin.readline())
        graph = defaultdict(list)
        for i in range(K):
            a, b = map(int, stdin.readline().split())
            graph[a].append(b)
            graph[b].append(a)
        def bfs(node):
            Q = deque()
            visited = set()
            result = 0
            Q.append(node)
            while Q:
                v = Q.popleft()
                visited.add(v)
                for i in graph[v]:
                    if i not in visited:
                        Q.append(i)
                        visited.add(i)
                        result += 1
            return result
        print(bfs(1))

if __name__ == "__main__":
    s = Solution()
    s.virus()