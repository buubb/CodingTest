from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_length = 0

    def diameterOfBinaryTree(self) -> int:
        def dfs(root:TreeNode) -> int:
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            self.max_length = max(self.max_length, left+right)
            return max(left, right) + 1

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        dfs(root)
        return self.max_length
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.diameterOfBinaryTree())
