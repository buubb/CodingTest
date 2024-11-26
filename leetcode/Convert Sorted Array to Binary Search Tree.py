
class TreeNode:
    def __init__(self, val=0, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArraryToBST(self, arr:list) -> TreeNode:
        if not arr:
            return None
        
        mid = len(arr) // 2

        node = TreeNode(arr[mid])
        node.left = self.sortedArraryToBST(arr[:mid])
        node.right = self.sortedArraryToBST(arr[mid+1:])

        return node


if __name__ == "__main__":
    arr = [-10, -7, -3, 0, 5, 7, 9]
    s = Solution()
    print(s.sortedArraryToBST(arr))