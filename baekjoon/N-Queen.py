import sys
input = sys.stdin.readline

class Solution:
    def __init__(self):
        self.cnt = 0

    def n_queen(self):
        n = int(input())
        visited = [False] * n
        left_diag = [False] * (2 * n)  # 왼쪽 대각선
        right_diag = [False] * (2 * n)  # 오른쪽 대각선

        def dfs(row):
            if row == n:
                self.cnt += 1
                return
            
            for col in range(n):
                if not visited[col] and not left_diag[row + col] and not right_diag[row - col + n - 1]:
                    visited[col] = left_diag[row + col] = right_diag[row - col + n - 1] = True
                    dfs(row + 1)
                    visited[col] = left_diag[row + col] = right_diag[row - col + n - 1] = False

        dfs(0)
        print(self.cnt)

if __name__ == "__main__":
    s = Solution()
    s.n_queen()
