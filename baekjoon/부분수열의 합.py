import sys
input = sys.stdin.readline

class Solution:
    def caculate(self):
        N, S = map(int,input().split())
        arr = list(map(int, input().split()))
        cnt = [0]
        def dfs(i, sub_sum):
            if i >= N:
                return
            sub_sum += arr[i]

            if sub_sum == S:
                cnt[0] += 1

            dfs(i+1, sub_sum)
            dfs(i+1, sub_sum - arr[i])
        dfs(0,0)
        print(cnt[0])
            
                

if __name__ == "__main__":
    s = Solution()
    s.caculate()