import sys, heapq
input = sys.stdin.readline

class Solution:
    def double_heapq(self):
        T = int(input())
        for _ in range(T):
            n = int(input())
            minhq = []
            maxhq = []
            deleted = [False] * n
            for i in range(n):
                o, m = input().split()
                m = int(m)
                
                if o == 'I':
                    heapq.heappush(minhq,(m,i))
                    heapq.heappush(maxhq,(-m,i))
                    
                elif o == 'D':
                    if m == 1:
                        while maxhq and deleted[maxhq[0][1]]:
                            heapq.heappop(maxhq)
                        if maxhq:
                            deleted[maxhq[0][1]] = True
                            heapq.heappop(maxhq)
                                
                    elif m == -1:
                        while minhq and deleted[minhq[0][1]]:
                            heapq.heappop(minhq)
                        if minhq:
                            deleted[minhq[0][1]] = True
                            heapq.heappop(minhq)

            while minhq and deleted[minhq[0][1]]:
                heapq.heappop(minhq)
            while maxhq and deleted[maxhq[0][1]]:
                heapq.heappop(maxhq)
            if not minhq or not maxhq:
                print("EMPTY")
            else: # 최대, 최소 출력 / heapq에서 첫번째 원소는 항상 최솟값
                print(-maxhq[0][0], minhq[0][0])


if __name__ == "__main__":
    s = Solution()
    s.double_heapq()