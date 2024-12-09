import sys
input = sys.stdin.readline

class Solution:
    def days_(self):
        E, S, M = map(int, input().split())
        year = 1
        while True:
            if (year-E) % 15 == 0 and (year-S) % 28 == 0 and (year-M) % 19 == 0:
                break
            year += 1
        print(year)

if __name__ == "__main__":
    s = Solution()
    s.days_()