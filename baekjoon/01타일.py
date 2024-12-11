import sys
input = sys.stdin.readline
max_int = 1_000_000
class Solution:
    def _01(self):
        N = int(input())
        f = [0] * (max_int+1)
        f[1], f[2] = 1, 2
        if N < 3:
            print(f[N])
            return
        for x in range(3,N+1):
            f[x] = (f[x-1] + f[x-2])%15746
        print(f[N])
        
if __name__ == "__main__":
    s = Solution()
    s._01()