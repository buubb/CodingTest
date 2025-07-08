import sys

input = sys.stdin.readline


class Solution:
    def answer(self):
        N = int(input())

        eggs = [] # 내구도, 무게

        for _ in range(N):
            eggs.append(list(map(int, input().split())))
        
        print(eggs)

        break_eggs = 0

        def backtracking(idx, k, visited):
            nonlocal break_eggs
            
            if idx == N:
                count = sum(1 for s, _ in eggs if s <= 0)
                break_eggs = max(break_eggs, count)
                return

            if eggs[idx][0] <= 0:
                backtracking(idx + 1)
                return

        
            for j in range(N):
                print(j)
                # j부터 시작하기
                if not visited[j] and j != idx and eggs[j][0] > 0:
                    # 내구도 = 현재 내구도 - 상대 계란 무게
                    eggs[idx][0], eggs[j][0] = eggs[idx][0] - eggs[j][1], eggs[j][0] - eggs[idx][1]
                    tmp = k
                    visited[idx] = True
                    backtracking(j, tmp, visited)
                    visited[idx] = False
                    eggs[idx][0], eggs[j][0] = eggs[idx][0] + eggs[j][1], eggs[j][0] + eggs[idx][1]
                    
        backtracking(0, 0, [False]*N)             
        print(break_eggs)





if __name__ == "__main__":
    s = Solution()
    s.answer()
