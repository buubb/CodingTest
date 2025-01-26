import sys, string
input = sys.stdin.readline

class Solution:
    def decrypt(self):
        cypher_text = input().rstrip()
        n = int(input())
        words = [input().rstrip() for _ in range(n)]
        alphabets = [char for char in string.ascii_lowercase]
        
        for start_idx in range(26):
            plain_text = ''
            for char in cypher_text:
                idx = alphabets.index(char) + start_idx
                if idx >= 26:
                    idx -= 26
                plain_text += alphabets[idx]
            for word in words:
                if word in plain_text:
                    print(plain_text)
                    return


if __name__ == "__main__":
    s = Solution()
    s.decrypt()