import sys
input = sys.stdin.readline

class Solution:
    def funny_func(self):
        dp = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
        for i in range(21):
            for j in range(21):
                for k in range(21):
                    if i <= 0 or j <= 0 or k <= 0:
                        dp[i][j][k] = 1
                    elif i < j and j < k:
                        dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1]-dp[i][j-1][k]
                    elif i == j == k:
                        dp[i][j][k] = 2**i
                    else:
                        dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]
            
        while True:
            a,b,c = map(int, input().split())
            res = 0
            if a == b == c == -1:
                break
            if a <= 0 or b <= 0 or c <= 0:
                res = 1
            elif a > 20 or b > 20 or c > 20:
                res = dp[20][20][20]
            else:
                res = dp[a][b][c]
            print(f"w({a}, {b}, {c}) = {res}")

            

if __name__ == "__main__":
    s = Solution()
    s.funny_func()