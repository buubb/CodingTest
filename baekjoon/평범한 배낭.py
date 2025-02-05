import sys
input = sys.stdin.readline

class Solution:
    def knapsack(self):
        n, k = map(int, input().split())
        cargo = [] # 무게, 가치
        for _ in range(n):
            w, v = map(int, input().split())
            cargo.append((w,v))
        pack = []
        for i in range(n+1):
            pack.append([])
            for c in range(k+1): # 무게
                if i==0 or c==0:
                    pack[i].append(0)
                elif cargo[i-1][0] <= c:
                    pack[i].append(
                        max(pack[i-1][c], pack[i-1][c-cargo[i-1][0]] + cargo[i-1][1])
                    )
                else:
                    pack[i].append(pack[i-1][c])
        print(pack)
        print(pack[-1][-1])

    def knapsack_(self):
        n,k = map(int, input().split())
        cargo = [] # w, v
        for _ in range(n):
            cargo.append(tuple(map(int, input().split())))
        
        dp = [0] * (k+1)
        for w, v in cargo:
            for i in range(k, w-1, -1):
                dp[i] = max(dp[i], dp[i-w] + v)
        
        print(dp[k])

if __name__ == "__main__":
    s = Solution()
    s.knapsack_()