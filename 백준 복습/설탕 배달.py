import sys
input = sys.stdin.readline
sys.setrecursionlimit
class Solution:
    # greedy
    def answer1(self):
        n = int(input())
        cnt = 0
        res = float('inf')
        if n < 5 and n != 3:
            print(-1)
            return
        
        while n >= 0:
            if n % 5 == 0 :
                cnt += n//5
                res = min(res, cnt)
                break
            n -= 3
            cnt += 1

        if res == float('inf'):
            print(-1)
        else:
            print(res)
            
    # dp
    def answer2(self):
        n = int(input())
        dp = [-1] * 5001
        dp[3], dp[4],dp[5] = 1, -1, 1
        for i in range(6, n+1):
            if i % 5 == 0:
                dp[i] = dp[i-5] + 1
            elif i % 3 == 0:
                dp[i] = dp[i-3] + 1
            elif dp[i-3] > 0 and dp[i-5] > 0:
                dp[i] = min(dp[i-5] + 1, dp[i-3] + 1)
        print(dp[n])
        

if __name__ == "__main__":
    s = Solution()
    s.answer1()

