import sys
input = sys.stdin.readline

class Solution:
    def answer(self):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        A.sort()
        B.sort(reverse=True)
        s = 0
        for i in range(N):
            s += A[i] * B[i]
        print(s)

if __name__ == "__main__":
    s = Solution()
    s.answer()