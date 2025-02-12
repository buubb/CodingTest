import sys, heapq
input = sys.stdin.readline

class Solution:
    def say_mid(self):
        N = int(input())
        arr = [int(input()) for _ in range(N)]
        res = [arr[0]]
        left, right = [], []
        mid = arr[0]
        for idx, num in enumerate(arr[1:], 1):
            if num < mid:
                heapq.heappush(left, -num)
            else:
                heapq.heappush(right, num)

            if idx % 2 == 1:
                if len(left) > len(right):
                    heapq.heappush(right, mid)
                    mid = -heapq.heappop(left)

            elif idx % 2 == 0:
                if len(left) > len(right):
                    heapq.heappush(right, mid)
                    mid = -heapq.heappop(left)
                elif len(left) < len(right):
                    heapq.heappush(left, -mid)
                    mid = heapq.heappop(right)
            res.append(mid)

        for r in res:
            print(r)

if __name__ == "__main__":
    s = Solution()
    s.say_mid()