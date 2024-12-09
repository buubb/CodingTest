import sys
import math
input = sys.stdin.readline

class Solution:
    def zoac(self):
        H, W, N, M = map(int, input().split())
        a = math.ceil(H/(N+1))
        b = math.ceil(W/(M+1))
        print(a*b)

if __name__ == "__main__":
    s = Solution()
    s.zoac()