import sys, heapq
input = sys.stdin.readline

class Solution:
    def mid_value(self):
        T = int(input())
        for _ in range(T):
            m = int(input()) # 수열의 크기
            arr = []
            for _ in range(m//10 + 1):
                a = list(map(int, input().split()))
                arr.extend(a)
            less = []
            more = []
            res = []
            res.append(arr[0])
            mid = arr[0]
            for idx, v in enumerate(arr[1:], 1):
                if v < mid:
                    heapq.heappush(less, -v)
                else:
                    heapq.heappush(more, v)
                
                if idx % 2 == 0:
                    if len(less) > len(more):
                        heapq.heappush(more, mid)
                        mid = -heapq.heappop(less)
                    elif len(less) < len(more):
                        heapq.heappush(less, -mid)
                        mid = heapq.heappop(more)

                    res.append(mid)
            print(len(res))
            for i in range(0, len(res), 10):
                print(*res[i:min(len(res), i+10)])
if __name__ == "__main__":
    s = Solution()
    s.mid_value()