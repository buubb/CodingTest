import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

class Solution:
    def short_route(self):
        V, E = map(int, input().split())
        start = int(input())
        INF = sys.maxsize
        graph = defaultdict(list)
        for _ in range(E):
            u, v, w = map(int, input().split())
            graph[u].append((w,v))
        distance = [INF] * (V+1) #최단 거리 테이블
        def dijkstra(start):
            hq = []
            heapq.heappush(hq,(0, start))
            distance[start] = 0
            
            while hq:
                w,v = heapq.heappop(hq)
                if distance[v] < w:
                    continue
                for (nw, nv) in graph[v]:
                    if w+nw < distance[nv]:
                        distance[nv] = w+nw
                        heapq.heappush(hq, (w+nw,nv))
        dijkstra(start)
        for i in range(1,V+1):
            if distance[i] == INF:
                print("INF")
            else:
                print(distance[i])
            



if __name__ == "__main__":
    s = Solution()
    s.short_route()