from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def __init__(self):
        self.depth = 0
    def univaluePath(self, root:TreeNode) -> int:
        def dfs(root:TreeNode) -> int:
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            if root.left and root.val == root.left.val:
                left += 1
            else:
                left = 0    
            if root.right and root.val == root.right.val:
                right += 1
            else:
                right = 0
            
            self.depth = max(self.depth, left + right)
            return max(left, right)
        dfs(root)
        return self.depth

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(5)
    sol = Solution()
    print(sol.univaluePath(root))