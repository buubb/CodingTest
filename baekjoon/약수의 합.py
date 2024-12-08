import sys
input = sys.stdin.readline

class Solution:
    def sumOfDivisors(self):
        max_int = 1000000
        dp = [0] * (max_int+1)
        s = [0] * (max_int+1)

        for i in range(1,max_int+1):
            j=1
            while i*j <= max_int:
                dp[i*j] += i
                j+=1
            s[i] = s[i-1] + dp[i]
        
        T = int(input())
        res = []
        for _ in range(T):
            n = int(input())
            res.append(str(s[n]))
        print('\n'.join(res))
            


if __name__ == "__main__":
    s = Solution()
    s.sumOfDivisors()