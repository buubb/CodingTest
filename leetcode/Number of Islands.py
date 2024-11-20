class Solution:
    def dfs(self, graph:list, i:int, j:int) -> int:
        if i < 0 or i >= len(graph) \
            or j < 0 or j>=len(graph[0]) \
            or graph[i][j] != 1:
            return
        
        graph[i][j] = 0 # 방문했다면 0으로 바꾼다.
        
        self.dfs(graph, i+1, j)
        self.dfs(graph, i-1, j)
        self.dfs(graph, i, j+1)
        self.dfs(graph, i, j-1)
    
    def numIslands(self, graph) -> int:
        if not graph:
            return 0
        count = 0
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if graph[i][j] == 1:
                    self.dfs(graph, i, j)
                    count += 1
        return count
    

class Solution2:
    def numIslands(self, graph) -> int:
        def dfs(i:int, j:int) -> int:
            if i < 0 or i >= len(graph) \
                or j < 0 or j>=len(graph[0]) \
                or graph[i][j] != 1:
                return
            
            graph[i][j] = 0 # 방문했다면 0으로 바꾼다.
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        if not graph:
            return 0
        count = 0
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if graph[i][j] == 1:
                    dfs(i, j)
                    count += 1
        return count

N = int(input())
arr = []
for i in range(N):
    a = [v for v in list(map(int,input()))]
    arr.append(a)

'''
예시)
4
11110
11010
11000
00000
'''

s = Solution2()
print(s.numIslands(arr))