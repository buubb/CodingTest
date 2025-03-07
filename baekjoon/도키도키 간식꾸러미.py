import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def answer(self):
        n = int(input())
        line = deque(map(int, input().split()))
        stack = []
        order = 1
        while line:
            
            if stack and stack[-1] == order:
                stack.pop()
                order += 1
            elif order == line[0]:
                line.popleft()
                order += 1
            elif order < line[0]:
                if not stack:
                    stack.append(line.popleft())
                else:
                    if stack[-1] < line[0]:
                        print("Sad")
                        return
                    else:
                        stack.append(line.popleft())
            

        while stack:
            if stack[-1] != order:
                print("Sad")
                return
            else:
                stack.pop()
                order += 1
        print("Nice")
        
if __name__ == "__main__":
    s = Solution()
    s.answer()