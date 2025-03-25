import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
class Solution:
    def answer(self):
        n = int(input())
        s = list(map(int, input().split()))
        s.sort()
        visited = set()
        
        def backtracking(sum, idx):
            if idx >= n:
                return
            
            if (sum, idx) in visited:
                return
            visited.add((sum, idx))
            possible_sums.add(sum + s[idx])
            backtracking(sum + s[idx], idx+1) # 선택했을 경우
            backtracking(sum, idx + 1) # 선택하지 않을 경우
                    
        possible_sums = set()
        backtracking(0, 0)
        for i in range(1, 1_000_000):
            if i not in possible_sums:
                print(i)
                break
if __name__ == "__main__":
    s = Solution()
    s.answer()