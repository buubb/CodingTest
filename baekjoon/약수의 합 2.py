import sys
input = sys.stdin.readline

class Solution:
    def sum_divisors(self):
        N = int(input())
        res = 0
        for i in range(1, N+1):
            res += (N//i)*i
        print(res)

if __name__ == "__main__":
    s = Solution()
    s.sum_divisors()