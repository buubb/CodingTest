import sys
input =sys.stdin.readline

class Solution:
    def nqueen(self):
        N = int(input())
        
        col = [False] * N
        # y = x
        diag1 = [False] * (2*N-1) # row + col
        # y = -x
        diag2 = [False] * (2*N-1) # row - col
        count = 0
        def backtracking(currentRow):
            nonlocal count
            if currentRow == N:
                count += 1
                return
            
            for j in range(N):
                if not col[j] and not diag1[currentRow+j] and not diag2[currentRow-j]:
                    col[j] = True
                    diag1[currentRow+j] = True
                    diag2[currentRow-j]=True

                    backtracking(currentRow+1)

                    col[j] = False
                    diag1[currentRow+j] = False
                    diag2[currentRow-j]=False
        
        backtracking(0)
        print(count)
if __name__ == "__main__":
    s = Solution()
    s.nqueen()