from collections import defaultdict
class Solution:
    dp = defaultdict(int)
    # 메모이제이션(top-down)
    def fib(self, n:int):
        if n <= 1:
            return n
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        return self.dp[n]
    
if __name__ == "__main__":
    s = Solution()
    print(s.fib(8))