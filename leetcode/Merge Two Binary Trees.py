
class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, T1, T2) -> list:
        merge = list()
        def dfs(T1, T2):
            if T1 and T2:
                merge.append(T1.val + T2.val)
                dfs(T1.left, T2.left)
                dfs(T1.right, T2.right)
            elif T1:
                merge.append(T1.val)
                dfs(T1.left, None)
                dfs(T1.right, None)
            elif T2:
                merge.append(T2.val)
                dfs(None, T2.left)
                dfs(None, T2.right)
        dfs(T1, T2)
        return merge

class Solution2:
    def mergeTrees(self, t1: TreeNode, t2:TreeNode) -> TreeNode:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)

            return node
        else:
            return t1 or t2    
        


if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree1.left = TreeNode(3)
    tree1.right = TreeNode(2)
    tree1.left.left = TreeNode(5)

    tree2 = TreeNode(2)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(3)
    tree2.left.right = TreeNode(4)
    tree2.right.right = TreeNode(7)

    s = Solution()
    print(s.mergeTrees(tree1, tree2))