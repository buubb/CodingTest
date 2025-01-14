import sys
from itertools import combinations
input = sys.stdin.readline

class Solution:
    def lotto(self):
        while True:
            arr = list(map(int, input().split()))
            if arr == [0]:
                break
            k = arr[0]
            for l in list(combinations(arr[1:],6)):
                print(*l)
            print("\n", end="")

if __name__ == "__main__":
    s = Solution()
    s.lotto()