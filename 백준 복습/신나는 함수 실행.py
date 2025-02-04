import sys
from collections import defaultdict
input = sys.stdin.readline

class Solution:
    dp = defaultdict(int)
    def funny_(self):
        while True:
            a,b,c = map(int, input().split())
            if a==-1 and b==-1 and c==-1:
                break
            
            def w(a,b,c):
                if self.dp[(a,b,c)]:
                    return self.dp[(a,b,c)]
                if a <= 0 or b <= 0 or c <= 0:
                    return 1
                elif a > 20 or b > 20 or c > 20:
                    if self.dp[(20, 20, 20)]:
                        return self.dp[(20, 20, 20)]
                    else:
                        self.dp[(a,b,c)] = w(20,20,20)
                elif a < b and b < c:
                    self.dp[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
                else:
                    self.dp[(a,b,c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
                return self.dp[(a,b,c)]
            
            print(f"w({a}, {b}, {c}) = {w(a,b,c)}")
if __name__ == "__main__":
    s = Solution()
    s.funny_()