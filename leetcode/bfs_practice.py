## 인접 리스트
graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3]
}

class Solution:
    def bfs_queue(self, graph:dict) -> list:
        discovered = [next(iter(graph))]
        queue = [next(iter(graph))]
        while queue:
            v = queue.pop(0)
            for w in graph[v]:
                if w not in discovered:
                    discovered.append(w)
                    queue.append(w)
        return discovered
    
solution = Solution()
print(solution.bfs_queue(graph))