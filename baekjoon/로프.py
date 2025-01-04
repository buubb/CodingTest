import sys, heapq
input = sys.stdin.readline

class Solution:
    def rope(self):
        N = int(input())
        ropes = []
        for _ in range(N):
            x = int(input())
            heapq.heappush(ropes, -x)
        result= 0
        for i in range(1,N+1):
            item = heapq.heappop(ropes)
            result = max(result, i*(-item))
        print(result)

if __name__ == "__main__":
    s = Solution()
    s.rope()
        

        
