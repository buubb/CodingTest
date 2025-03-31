import sys
input = sys.stdin.readline

class Solution:
    def caculate(self, visited, n, grid):

        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += grid[i][j]
                elif not visited[i] and not visited[j]:
                    link += grid[i][j]
        return abs(start-link)
    
    def answer(self):
        N = int(input()) # 사람 수
        grid = [list(map(int, input().split())) for _ in range(N)]
        
        # power: Sij + Sji
        result = float('inf')
        visited = [False] * N
        def backtracking(person, visited):
            nonlocal result
            if person == N-1:
                result = min(result, self.caculate(visited, N, grid))
                return
            for i in range(person, N):
                if not visited[i]:
                    visited[i] = True
                    backtracking(i, visited)
                    visited[i] = False
                    
            
        backtracking(0, visited)
        print(result)
if __name__ == "__main__":
    s = Solution()
    s.answer()