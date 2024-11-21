from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times, N:int, K:int) -> int:
        graph = defaultdict(list)
        for u, v, w in times: # u: 출발지, v: 도착지, w: 시간
            graph[u].append((v,w))
        Q = [(0,K)]
        dist = defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt,v))
        
        if len(dist) == N:
            return max(dist.values())
        return -1
        

s = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
print(s.networkDelayTime(times, N, K))