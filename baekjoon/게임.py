import sys
from fractions import Fraction
input = sys.stdin.readline
max_int = 1_000_000_000
class Solution:
    def game_(self):
        X, Y = map(int, input().split())
        Z = int(Fraction(Y,X)*100) # (100*Y) // X 도 가능하다..
        left, right = 1, max_int
        res=-1
        while left <= right:
            mid = left + (right-left) // 2
            x, y = X + mid, Y + mid
            z = int(Fraction(y,x)*100)
            # print(f"mid: {mid}, x: {x}, y: {y}, z: {z} Z:{Z}")
            if z > Z:
                res = mid
                right = mid - 1
            elif z <= Z:
                left = mid + 1
        print(res)

if __name__ == "__main__":
    s = Solution()
    s.game_()