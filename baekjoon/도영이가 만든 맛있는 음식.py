import sys
input = sys.stdin.readline

class Solution:
    def doyoung_food(self):
        T = int(input())
        s = b = 0
        for _ in range(T):
            S, B = map(int, input().split())
            s = s | (1 << S-1)
            print(s)
            b = b | (1 << B-1)
        print(s)
        print(b)
if __name__ == "__main__":
    s = Solution()
    s.doyoung_food()