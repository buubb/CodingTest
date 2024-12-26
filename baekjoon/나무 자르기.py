import sys
input = sys.stdin.readline

class Solution:
    def slicing_tree(self):
        N, M = map(int, input().split())
        trees = [tree for tree in map(int, input().split())]
        left = 1
        right = max(trees)
        result = 0
        while left <= right:
            mid = left + (right - left) // 2
            sum = 0
            for tree in trees:
                if tree > mid:
                    sum += tree - mid
           
            if sum < M:
                right = mid - 1
            elif sum >= M:
                result = mid
                left = mid + 1
            
        return result


if __name__ == "__main__":
    s = Solution()
    res = s.slicing_tree()
    print(res)