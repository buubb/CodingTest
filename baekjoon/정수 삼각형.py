import sys
input = sys.stdin.readline
from collections import deque
class Solution:
    def triagle(self):
        N = int(input())
        graph = []
        max_matrix = [[] for _ in range(N)]
        for _ in range(N):
            graph.append(list(map(int, input().split())))
        
        for i in range(N-1, -1, -1):
            for j in range(len(graph[i])):
                if i == N-1:
                    max_matrix[i].append(graph[i][j])
                else:
                    max_matrix[i].append(graph[i][j] + max(max_matrix[i+1][j], max_matrix[i+1][j+1]))
        print(max_matrix[0][0])
if __name__ == "__main__":
    s = Solution()
    s.triagle()