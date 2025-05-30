from collections import defaultdict
# bruteforce 풀이
# class Solution1:
#     def palindromePairs(self, words:list) -> list:
#         def is_palindrome(word):
#                 return word == word[::-1]
        
#         output = []
#         for i, word1 in enumerate(words):
#             for j, word2 in enumerate(words):
#                 if i == j:
#                     continue
                  
#                 if is_palindrome(word1 + word2):
#                     output.append([i,j])

#         return output
    
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word:str) -> bool:
        return word[::] == word[::-1]
    
    def insert(self, index, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word)-i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    def search(self, index, word) -> list:
        result = []
        node = self.root

        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result
    
class Solution2:
    def palindromePairs(self, words:list) -> list:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i,word)
        
        results =[]
        for i, word in enumerate(words):
            results.extend(trie.search(i,word))

        return results
    
if __name__ == "__main__":
    s = Solution2()
    words = ['d', 'dcbbc','bbcd','cbcd','dcbb']
    #words = ['bat','tab','cat']
    #words = ['abcd', 'dcba','lls','s','sssll']
    print(s.palindromePairs(words))