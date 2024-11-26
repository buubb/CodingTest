
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result : int = 0
    def sumOfBST(self, root:TreeNode, L:int, R:int) -> int:
        if not root:
            return 0
        if L <= root.val <= R:
            self.result += root.val
            self.sumOfBST(root.left, L, R)
            self.sumOfBST(root.right, L, R)
        elif L > root.val:
            self.sumOfBST(root.right, L, R)
        elif R < root.val:
            self.sumOfBST(root.left, L, R)
        return self.result
        
    def rangeSumBST(self, root:TreeNode, L:int, R:int) -> int:
        if not root:
            return 0
        
        return (root.val if L <= root.val <= R else 0) + \
                self.rangeSumBST(root.left, L, R) + \
                self.rangeSumBST(root.right, L, R)
     
    def rangeSumBST_(self, root:TreeNode, L:int, R:int) -> int:
        def dfs(node:TreeNode):
            if not node:
                return 0
            
            if L > node.val:
                return dfs(node.right)
            elif R < node.val:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)
        
        return dfs(root)

    def _rangeSumBST(self, root:TreeNode, L:int, R:int) -> int:
        stack, sum = [root], 0
        while stack:
            node = stack.pop()
            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val < R :
                    stack.append(node.right)
                if L <= node.val <= R:
                    sum += node.val
        return sum

if __name__ == "__main__":

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)

    s = Solution()
    print(s.sumOfBST(root, 7, 15))
    print(s.rangeSumBST(root, 7, 15))
    print(s.rangeSumBST_(root, 7, 15))
    print(s._rangeSumBST(root, 7, 15))
