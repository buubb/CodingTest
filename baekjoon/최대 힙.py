import sys, heapq
input = sys.stdin.readline
class Solution:
    def max_heap(self):
        N = int(input())
        hq = []
        for _ in range(N):
            x = int(input())
            if x == 0:
                if not hq:
                    print(0)
                else:
                    print(-heapq.heappop(hq))
                continue
            heapq.heappush(hq, -x)
if __name__ == "__main__":
    s = Solution()
    s.max_heap()
            

