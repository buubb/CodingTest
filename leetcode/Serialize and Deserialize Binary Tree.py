from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def serialize_(self, tree:TreeNode) -> str:
        Q = deque()
        result = []
        Q.append(None)
        Q.append(tree)
        while Q:
            node = Q.popleft()
            if node:
                Q.append(node.left)
                Q.append(node.right)
                result.append(str(node.val))
            else:
                result.append("#")

        return ''.join(result)
    
    def deserialize_(self, char:str) -> TreeNode:
        graph = list(char)
        index = 2
        root = TreeNode(graph[1])
        Q = deque([root])
        while Q:
            node = Q.popleft()
        
            if graph[index] != "#":
                node.left = TreeNode(graph[index])
                Q.append(node.left)
            index += 1
            if graph[index] != "#":
                node.right = TreeNode(graph[index])
                Q.append(node.right)
            index += 1

        return root

        


if __name__ == "__main__":
    root = TreeNode("A")
    root.left = TreeNode("B")
    root.right = TreeNode("C")
    root.right.left = TreeNode("D")
    root.right.right = TreeNode("E")

    s = Solution()
    print(s.serialize_(s.deserialize_(s.serialize_(root))))