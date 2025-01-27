import sys
from collections import defaultdict
input = sys.stdin.readline

class Solution:
    def decrypt(self):
        key = input().strip()
        cypher_text = input().strip()
        key_len, cypher_len = len(key), len(cypher_text)
        cypher_grid = defaultdict(list)
        i = 0
        for k in sorted(key):
            cypher_grid[k].append(cypher_text[i:i+cypher_len//key_len])
            i+=cypher_len//key_len
        
        plain_text = ''
        
        for i in range(cypher_len//key_len):
            check = defaultdict(int)
            for k in key:
                plain_text += cypher_grid[k][check[k]][i]
                check[k] += 1
        print(plain_text)
        

if __name__ == "__main__":
    s = Solution()
    s.decrypt()