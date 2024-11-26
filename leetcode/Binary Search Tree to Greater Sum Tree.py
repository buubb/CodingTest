
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    val : int = 0
    
    def greaterSumTree(self, root:TreeNode) -> TreeNode:
        if root:
            self.greaterSumTree(root.right)
            self.val += root.val
            root.val = self.val
            print(root.val)
            self.greaterSumTree(root.left)
        return root

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(3)
    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)
    
    s = Solution()
    s.greaterSumTree(root)