import sys
from collections import Counter
input = sys.stdin.readline

class Solution:
    def find_number(self):
        N = int(input())
        A = list(map(int, input().split()))
        M = int(input())
        B = list(map(int, input().split()))
        dic_A = Counter(A)
        for i in range(M):
            print(dic_A[B[i]], end=" ")
        print()

if __name__ == "__main__":
    s = Solution()
    s.find_number()