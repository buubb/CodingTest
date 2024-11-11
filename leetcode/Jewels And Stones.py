from collections import defaultdict, Counter

class Solution1:
    def numJewelsInStones(self, J:str, S:str) -> int:
        freqs = {}
        for char in S:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1
        sum = 0
        for char in J:
            sum += freqs[char]
        return sum

class Solution2:
    def numJewelsInStones(self, J:str, S:str) -> int:
        freqs = defaultdict(int)
        for char in S:
            freqs[char] += 1
        sum = 0
        for char in J:
            sum += freqs[char]
        return sum
    
class Solution3:
    def numJewelsInStones(self, J:str, S:str) -> int:
        freqs = Counter(S)
        sum = 0
        for char in J:
            sum += freqs[char]
        return sum
    
class Solution4:
    def numJewelsInStones(self, J:str, S:str) -> int:
        return sum([s in J for s in S])

J = "aA"
S = "aAAbbbb"
solution = Solution4()
print(solution.numJewelsInStones(J,S))