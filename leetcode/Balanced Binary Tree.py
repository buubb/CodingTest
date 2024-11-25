class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, left:TreeNode, right:TreeNode) -> bool:
        def dfs(node:TreeNode) -> int:
            if node.left:
                return dfs(node.left) + 1
            elif node.right:
                return dfs(node.right) + 1
            else:
                return 0
        L = dfs(left)
        R = dfs(right)
        if abs(L-R) > 1:
            return False
        else:
            return True 
class Solution2:
    def isBalanced(self, root:TreeNode) -> bool:
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            right = check(root.right)

            if left == -1 \
                or right == -1 \
                    or abs(left-right) > 1:
                return -1
            return max(left, right) + 1
        return check(root) != -1
    
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    s = Solution()
    s2 = Solution2()
    print(s.isBalanced(root.left, root.right))
    print(s2.isBalanced(root2))