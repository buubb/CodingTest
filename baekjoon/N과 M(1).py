import sys
input = sys.stdin.readline
from itertools import permutations
class Solution:
    def n_m(self):
        N, M = map(int, input().split())
        for i in permutations(range(1,N+1),M):
            print(*i)

if __name__ == "__main__":
    s = Solution()
    s.n_m()