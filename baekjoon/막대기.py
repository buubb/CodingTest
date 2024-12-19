import sys
input = sys.stdin.readline

class Solution:
    def stick(self):
        X = int(input())
        cnt = 0
        while X > 0:
            X = X & (X-1)
            cnt += 1
        print(cnt)
        # if X <= N:
        #     print(bin(X).count('1')) 파이썬 내장 함수 활용

if __name__ == "__main__":
    s = Solution()
    s.stick()