import sys

input = sys.stdin.readline

class Solution:
    def answer(self):
        N = int(input())
        t_arr = [0]
        p_arr = [0]
        k_arr = [0] # (t-i) - 1

        for i in range(N):
            t, p = map(int, input().split())
            idx = i + 1
            t_arr.append(t) # time
            p_arr.append(p) # pay
            k_arr.append(t+idx-1)
        
        max_pay = 0
        def backtracking(i, bef_k, pay):
            nonlocal max_pay

            max_pay = max(max_pay, pay)

            for j in range(i, N+1):
                if k_arr[j] < (N+1) and j > bef_k:
                    backtracking(j, k_arr[j], pay + p_arr[j])
        
        backtracking(0, 0, 0)
        print(max_pay)        


    def answer_dp(self):
        N = int(input())

        schedule = []
        for i in range(N):
            t, p = map(int, input().split())
            schedule.append([t,p])

        schedule.reverse()
        schedule.insert(0, [])

        # print(schedule)

        dp = [0] * (N+1)

        for i in range(1, N+1):
            if i < schedule[i][0]:
                dp[i] = dp[i-1]
            else:
                dp[i] = max(dp[i-1], schedule[i][1] + dp[i-schedule[i][0]]) 

        print(dp[N])


if __name__ == "__main__":
    s = Solution()
    s.answer_dp()