import sys
input = sys.stdin.readline

class Solution:
    def divisior(self):
        N = int(input())
        divisors = [int(i) for i in input().split()]
        
        div = sorted(divisors)
        if N == 1:
            print(div[0]**2)
        else:
            print(div[0]*div[-1])

if __name__ == "__main__":
    s = Solution()
    s.divisior()