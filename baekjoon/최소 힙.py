import sys, heapq
input = sys.stdin.readline

class Solution:
    def heap_(self):
        N = int(input())
        h = []
        
        for _ in range(N):
            n = int(input())
            if n == 0:
                if len(h) != 0:
                    print(heapq.heappop(h))
                else:
                    print(0)
            else:
                heapq.heappush(h,n)
        
if __name__ == "__main__":
    s = Solution()
    s.heap_()