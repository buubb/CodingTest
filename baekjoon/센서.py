import sys, heapq
input = sys.stdin.readline

class Solution:
    def sensor(self):
        N = int(input())
        K = int(input())
        sensor = list(map(int,input().split()))
        sensor.sort()
        diff = []
        for i in range(1,N):
            heapq.heappush(diff, sensor[i-1]-sensor[i])
        for _ in range(K-1):
            if diff:
                heapq.heappop(diff)
        print(-sum(diff))

if __name__ == "__main__":
    s = Solution()
    s.sensor()