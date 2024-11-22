from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def invertTree(self, root:TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
    
class Solution2:
    def invertTree(self, root:TreeNode) -> TreeNode:
        Q = deque([root])

        while Q :
            node = Q.popleft()
            if node:
                node.left, node.right = node.right, node.left
                Q.append(node.left)
                Q.append(node.right)
        return root

class Solution3:
    def invertTree(self, root:TreeNode) -> TreeNode:
        stack = deque([root])

        while stack:
            node = stack.pop()

            if node:
                node.left , node.right = node.right = node.left

                stack.append(node.left)
                stack.append(node.right)
        return root


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    sol = Solution()
    print(sol.invertTree(root))