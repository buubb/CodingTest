from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n:int, edges:list, src:int, dst:int, K:int) -> int:
        graph = defaultdict(list)
        for s, d, p in edges:
            graph[s].append((d,p))
        
        # (가격, 정점, 남은 경유지 수)
        Q = [(0, src, K)]
        while Q:
            price, v , k= heapq.heappop(Q)
            if v == dst:
                return price
            if k >= 0:
                for d,p in graph[0]:
                    alt = price + p
                    heapq.heappush(Q, (alt,d,k-1))
        return -1

s = Solution()
n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
K = 0
print(s.findCheapestPrice(n, edges, src, dst, K))