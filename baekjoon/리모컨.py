import sys, bisect
from itertools import combinations
input = sys.stdin.readline

class Solution:
    def remote(self):
        n = input().rstrip()
        m = int(input())
        broken = tuple(map(int, input().split()))
        
        first_cnt = abs(100-int(n))
        for num in range(1_000_000):
            for i in str(num):
                if int(i) in broken:
                    break
            else:
                first_cnt = min(first_cnt, len(str(num)) + abs(int(n) - num))
                
        print(first_cnt)


if __name__ == "__main__":
    s = Solution()
    s.remote()