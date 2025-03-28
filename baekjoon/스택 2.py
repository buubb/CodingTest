import sys
input = sys.stdin.readline

class solution:
    def answer(self):
        stack = []
        for _ in range(int(input())):
            command = list(map(int, input().split()))
            m = command[0]
            if m == 1:
                try:
                    stack.append(command[1])
                except:
                    pass       
            elif m == 2:
                print(stack.pop() if stack else -1)
            elif m == 3:
                print(len(stack))
            elif m==4:
                print(1 if not stack else 0)
            elif m==5:
                print(stack[-1] if stack else -1)

if __name__ == "__main__":
    s = solution()
    s.answer()