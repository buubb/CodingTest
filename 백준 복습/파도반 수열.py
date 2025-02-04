import sys
input = sys.stdin.readline

class Solution:
    def wave_(self):
        T = int(input())
        for _ in range(T):
            n = int(input())
            if n <= 3:
                print(1)
                continue
            p = [0] * (n+1)
            p[1], p[2], p[3] = 1, 1, 1
            for x in range(4, n+1):
                p[x] = p[x-2] + p[x-3]
            print(p[n])

if __name__ == "__main__":
    s = Solution()
    s.wave_()