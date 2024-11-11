class Solution:
    def result(self, S:str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(S):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)
            used[char] = index
        return max_length
    