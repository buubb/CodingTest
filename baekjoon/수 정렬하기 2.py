import sys
input = sys.stdin.readline

class Solution:
    def sort_num(self):
        N = int(input())
        nums = [int(input()) for _ in range(N)]
        for i in sorted(nums):
            print(i)

if __name__ == "__main__":
    s = Solution()
    s.sort_num()