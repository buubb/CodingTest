import sys
from collections import defaultdict
input = sys.stdin.readline

class Solution:
    def decrypt(self):
        key = input().strip()
        cyphertext = input().strip()
        grid = defaultdict(list)
        i = 0
        column = len(cyphertext)//len(key)

        for k in sorted(key):
            grid[k].append(cyphertext[i:i+column])
            i += column
        #print(grid)

        for i in range(column):
            check = defaultdict(int) # 키의 각 문자 사용 횟수
            for k in key:
                print(grid[k][check[k]][i], end='')
                check[k] += 1

if __name__ == "__main__":
    s = Solution()
    s.decrypt()
