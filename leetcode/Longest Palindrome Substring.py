class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 and s == s[::-1]:
            return s
        
        def expand(left:int , right:int) -> str:
            while left >=0 and right<len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return s[left + 1:right]

        result = ''
        for i in range(0, len(s)-1):
            result = max(result, expand(i, i+2), expand(i, i+1), key=len)
        
        return result
