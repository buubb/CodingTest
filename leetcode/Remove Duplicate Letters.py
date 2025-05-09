from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s:str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char,''))
        return ''
    
class Solution2:
    def removeDuplicateLetters(self, s:str)->str:
        counter, seen, stack = Counter(s), set(), []

        for char in s:
            counter[char] -=1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                print(stack[-1])
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)

char = 'cbacdcbc'
solution = Solution2()
print(solution.removeDuplicateLetters(char))