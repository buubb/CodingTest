import sys
input = sys.stdin.readline

class Solution:
    def chess(self):
        M,N = map(int, input().split())
        chess = []
        for _ in range(M):
            chess.append(list(input().strip()))

        min_value = 64
        for i in range(M-7):
            for j in range(N-7):
                res1 = 0
                res2 = 0
                for a in range(i,8+i):
                    for b in range(j,8+j):
                        if (a+b) % 2 == 0:
                            if chess[a][b] != 'W':
                                res1 += 1
                            else:
                                res2 += 1
                            
                        else:
                            if chess[a][b] != 'B':
                                res1 += 1
                            else:
                                res2 += 1   
                            
                min_value = min(res1, res2, min_value)
        
        
        print(min_value)


        


if __name__ == "__main__":
    s = Solution()
    s.chess()