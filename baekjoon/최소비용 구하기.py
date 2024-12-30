import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

class Solution:
    def min_cost(self):
        N = int(input())
        M = int(input())
        INF = sys.maxsize
        graph = defaultdict(list)
        for _ in range(M):
            sv, dv, w = map(int, input().split())
            graph[sv].append((dv,w))
        start, target = map(int, input().split())
        dist = [INF] * (N+1)
        def dijkstra(start):
            hq = []
            heapq.heappush(hq, (0, start))
            dist[start] = 0
            while hq:
                w, v = heapq.heappop(hq)
                if w > dist[v]:
                    continue
                for (nv, nw) in graph[v]:
                    cost = w + nw
                    if dist[nv] > cost:
                        dist[nv] = cost
                        heapq.heappush(hq, (cost, nv))
        dijkstra(start)
        print(dist[target])

            

if __name__ == "__main__":
    s = Solution()
    s.min_cost()