import sys
input = sys.stdin.readline

class Solution:
    def sum_123(self):
        T = int(input())
        f = [0] * 12
        f[1], f[2], f[3]= 1,2,4
        for x in range(4, len(f)):
            f[x] = f[x-1] + f[x-2] + f[x-3]
        
        for _ in range(T):
            N = int(input())
            print(f[N])

if __name__ == "__main__":
    s = Solution()
    s.sum_123()