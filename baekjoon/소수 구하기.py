import sys
input = sys.stdin.readline

class Solution:
    def demical_(self):
        M, N = map(int, input().split())
        for i in range(M, N+1):
            isPrime = True
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    isPrime = False
                    break
            if isPrime:
                print(i)


if __name__ == "__main__":
    s = Solution()
    s.demical_()