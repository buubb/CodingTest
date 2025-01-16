import sys
input = sys.stdin.readline

class Solution:
    def doyoung_food(self):
        T = int(input())
        arr = [tuple(map(int, input().split())) for _ in range(T)]
        res = sys.maxsize
        for i in range(1,1<<T): #1<<T는 2의 T승, 재료는 1가지 이상이므로 1부터 시작
            bit = list(map(int, bin(i)[2:].zfill(T)))
            total_s = 1
            total_b = 0
            for j in range(T):
                s,b=arr[j]
                if bit[j]:
                    total_s *= s
                    total_b += b
            res = min(res, abs(total_s - total_b))
        print(res)
if __name__ == "__main__":
    s = Solution()
    s.doyoung_food()