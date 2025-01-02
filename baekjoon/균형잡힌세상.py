import sys
input = sys.stdin.readline

class Solution:
    def world(self):
        while True:
            char = input().rstrip()
            if char == '.':
                return
            graph = {
                ')' : '(',
                ']' : '['
            }
            stack = []
            isOk = True
            for c in char:
                if c =='(' or c== '[':
                    stack.append(c)
                elif c in graph:
                    if not stack:
                        isOk = False
                        break
                    k = stack.pop()
                    if k != graph[c]:
                        isOk = False
                        break
            if stack:
                isOk = False
            print("yes" if isOk else "no")

                
if __name__ == "__main__":
    s = Solution()
    s.world()