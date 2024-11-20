class Solution:
    def letterCombinations(self, digits:list):
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            for i in range(index, len(digits)):
                for j in letter[digits[i]]:
                    dfs(i+1, path+j)


        if not digits:
            return []
        
        letter = {
            2 : 'abc',
            3 : 'def',
            4 : 'ohi',
            5 : 'jkl',
            6 : 'mno',
            7 : 'pqrs',
            8 : 'tuv',
            9 : 'wxyz'
        }

        result = []
        dfs(0, "")

        return result
    

digits = list(map(int, input()))        
s = Solution()
print(s.letterCombinations(digits))

