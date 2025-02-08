import sys, heapq
input = sys.stdin.readline

class Solution:
    def double_heapq(self):
        t = int(input())
        for _ in range(t):
            k = int(input())
            min_hq = []
            max_hq = []
            deleted = [False] * k
            for i in range(k):
                op, n = input().split()
                n = int(n)
                if op == 'I':
                    heapq.heappush(min_hq, (n, i))
                    heapq.heappush(max_hq, (-n, i))
                elif op == 'D':
                    if not max_hq or not min_hq:
                        continue
                    
                    if n == 1:
                        while max_hq and deleted[max_hq[0][1]]:
                            heapq.heappop(max_hq)
                        if max_hq:
                            deleted[max_hq[0][1]] = True
                            heapq.heappop(max_hq)
                        
                    elif n == -1:
                        while min_hq and deleted[min_hq[0][1]]:
                            heapq.heappop(min_hq)
                        if min_hq:
                            deleted[min_hq[0][1]] = True
                            heapq.heappop(min_hq)
            
            while max_hq and deleted[max_hq[0][1]]:
                heapq.heappop(max_hq)
            while min_hq and deleted[min_hq[0][1]]:
                heapq.heappop(min_hq)
                    
            if min_hq and max_hq:
                print(-max_hq[0][0], min_hq[0][0])
            else:
                print("EMPTY")


if __name__ == "__main__":
    s = Solution()
    s.double_heapq()