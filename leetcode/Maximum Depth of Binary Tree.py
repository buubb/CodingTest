from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTree(self, root:TreeNode) -> int:
        if root is None:
            return 0
        Q = deque([root])
        depth = 0

        while Q:
            depth += 1
            for i in range(len(Q)):
                cur_root = Q.popleft()
                if cur_root.left:
                    Q.append(cur_root.left)
                if cur_root.right:
                    Q.append(cur_root.right)
        return depth

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = None
    root.left.right = None
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    sol = Solution()
    result = sol.binaryTree(root)
    print(result)