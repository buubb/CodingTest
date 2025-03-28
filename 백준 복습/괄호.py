import sys
input = sys.stdin.readline

class Solution:
    def answer(self):
        for _ in range(int(input())):
            arr = list(input().strip())
            stack = []
            for a in arr:
                if a == ')':
                    try:
                        stack.pop()
                    except:
                        print("NO")
                        break
                else:
                    stack.append(a)
            else:
                print("NO" if stack else "YES")

if __name__ == "__main__":
    s = Solution()
    s.answer()