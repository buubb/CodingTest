import bisect
class Solution:
    def findContentChildren(self, g:list, s:list):
        g.sort()
        s.sort()

        child_i = cookie_j = 0
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1
        return child_i
    
    def findContentChildren2(self, g:list, s:list):
        g.sort()
        s.sort()

        child_i = 0
        for i in s:
            index = bisect.bisect_right(g, i)
            if index > child_i:
                child_i += 1
        return child_i


if __name__ == "__main__":
    s = Solution()
    g = [1,2,3]
    k = [1,1]
    print(s.findContentChildren2(g,k))