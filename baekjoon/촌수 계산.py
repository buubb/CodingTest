from sys import stdin
from collections import defaultdict, deque
class Solution:
    def family(self):
        N = int(stdin.readline())
        a,b = map(int, stdin.readline().split())
        M = int(stdin.readline())
        grid = defaultdict(list)
        for _ in range(M):
            parent, child = map(int, stdin.readline().split())
            grid[parent].append(child)
            grid[child].append(parent)
        
        def bfs(node):
            Q = deque()
            Q.append((node, 0))  # (현재 노드, 현재 거리)
            visited = set()
            visited.add(node)
            while Q:
                v, res = Q.popleft()
                if v == b:
                    return res
                for i in grid[v]:
                    if i not in visited:
                        Q.append((i, res+1))
                        visited.add(i)
            
            return -1
            
        print(bfs(a))
        

if __name__ == "__main__":
    s = Solution()
    s.family()