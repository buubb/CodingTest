import sys
input = sys.stdin.readline

class Solution:
    def movie(self):
        n = int(input())
        cnt = 0
        for k in range(10_000_000):
            str_k = str(k)
            if '666' in str_k:
                cnt += 1
                if cnt == n:
                    print(k)
                    break

if __name__ == "__main__":
    s = Solution()
    s.movie()