import sys
from collections import defaultdict
input = sys.stdin.readline

class Solution:
    def __init__(self):
        self.leaf = 0

    def tree(self):
        N = int(input())
        tree = list(map(int, input().split()))
        d = int(input())

        # 그래프 생성 및 루트 노드 찾기
        graph = defaultdict(list)
        root = -1
        for child, parent in enumerate(tree):
            if parent == -1:
                root = child
            else:
                if child != d: # child에 삭제할 노드를 넣지 않으면, dfs 실행 시 해당 노드부터 방문하지 않게 됨됨
                    graph[parent].append(child)

        def cnt_leaves(node):
            if not graph[node]:
                self.leaf += 1
                return
            for n in graph[node]:
                cnt_leaves(n)

        # 루트가 삭제된 경우 처리
        if root != d:
            cnt_leaves(root)

        print(self.leaf)

if __name__ == "__main__":
    s = Solution()
    s.tree()
