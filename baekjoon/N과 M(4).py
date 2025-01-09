import sys
from itertools import product
input = sys.stdin.readline

class Solution:
    def n_m3(self):
        n,m = map(int, input().split())
        for x in product([i for i in range(1,n+1)], repeat=m):
            isOk = True
            for i in range(1, m):
                if x[i] < x[i-1]:
                    isOk = False
                    break
            if isOk:
                print(*x)

if __name__ == "__main__":
    s = Solution()
    s.n_m3()