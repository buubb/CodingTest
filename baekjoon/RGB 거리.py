import sys
input = sys.stdin.readline

class Solution:
    def rgb_(self):
        N = int(input())
        arr = []
        for _ in range(N):
            arr.append(list(map(int, input().split())))
        dp = [[0]*3 for _ in range(N)]
        dp[0][0], dp[0][1], dp[0][2] = arr[0][0], arr[0][1], arr[0][2]
        
        for i in range(1,N):
            for j in range(3):
                k = 0
                if j == 0:
                    k = min(dp[i-1][1], dp[i-1][2])
                elif j == 1:
                    k = min(dp[i-1][0], dp[i-1][2])
                elif j == 2:
                    k = min(dp[i-1][0], dp[i-1][1])
                dp[i][j] = k + arr[i][j]
        
        res = min(dp[N-1])
        print(res)

if __name__ == "__main__":
    s = Solution()
    s.rgb_()