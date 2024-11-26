from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, N:int, edges:list) -> list:
        graph = defaultdict(list)
        min_cnt = N
        root = []
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = [False] * N
        def dfs(node, visited) -> int:
            visited[node] = True
            max_depth = 0

            for n in graph[node]:
                if not visited[n]:
                    depth = dfs(n, visited)
                    max_depth = max(max_depth, depth)
            return max_depth + 1
            
        for i in range(N):
            visited = [False] * N
            cnt = dfs(i, visited)
            
            if min_cnt > cnt:
                min_cnt = cnt
                root = [i] # 새로운 값이면 리스트 초기화 후 추가
            elif cnt == min_cnt:
                root.append(i)
        return root

class Solution2: # 리프 노드를 제거해 나가는 방법 -> 효율적
    def findMinHeightTrees(self, n:int, edges:list) -> list:
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        print(graph)
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves
    
if __name__ == "__main__":
    # N = 4
    # edges = [[1,0],[1,2],[1,3]]
    
    N= 6
    edges = [[0,3],[1,3],[2,3],[4,3], [5,4]]
    s = Solution2()
    print(s.findMinHeightTrees(N, edges))