import sys
from itertools import permutations
import string
input = sys.stdin.readline

class Solution:
    def answer(self):
        while True:
            str = input().rstrip()

            if str == 'end':
                return
            
            alpha = ['a','e','i','o','u'] # 모음
            arr = []

            for s in str:
                if s in alpha:
                    arr.append('0')
                else:
                    arr.append('1')
            
            isAccept = True
            for i in range(len(str)-1):
                if str[i] == str[i+1]:
                    if str[i] not in ('e', 'o'):
                        isAccept = False
                        break
            
            bool_str = ''.join(arr)
            if '0' not in bool_str or '000' in bool_str or '111' in bool_str or not isAccept:
                print(f"<{str}> is not acceptable.")
            else:
                print(f"<{str}> is acceptable.")


if __name__ == "__main__":
    s = Solution()
    s.answer()