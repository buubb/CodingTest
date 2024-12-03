
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
class Solution:
    def whereIsParent(self):
        N = int(sys.stdin.readline())
        graph = defaultdict(list)
        res = [0] * (N + 1)  # 부모 정보를 저장할 배열
        for _ in range(N-1):
            a,b = map(int, sys.stdin.readline().split())
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):
            for i in graph[node]:
                if res[i] == 0:  # 부모 노드는 방문하지 않음
                    res[i] = node
                    dfs(i)

        dfs(1)
        for i in range(2, N+1):
            print(res[i])

    
if __name__ == "__main__":
    s = Solution()
    s.whereIsParent()

            

