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
    def dfs_stack(self, graph:dict):
        discovered = []
        stack = [next(iter(graph))] # list(graph.keys())[0]도 가능
        while stack:
            v = stack.pop()
            if v not in discovered:
                discovered.append(v)
                for w in graph[v]:
                    stack.append(w)
        return discovered

    def dfs_recurs(self, graph:dict, v, discovered = []) -> list:
        discovered.append(v)
        for w in graph[v]:
            if w not in discovered:
                discovered = self.dfs_recurs(graph, w, discovered)
        return discovered


solution = Solution()

# dfs_stack 호출
print(solution.dfs_stack(graph))

# dfs_recurs 호출
print(solution.dfs_recurs(graph, next(iter(graph))))