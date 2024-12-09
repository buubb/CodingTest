import sys
input = sys.stdin.readline

class Solution:
    def generate(self):
        N = int(input())
        s = set()
        for _ in range(N):
            cmd = list(input().split())
            if cmd[0] == "add":
                if int(cmd[1]) not in s:
                    s.add(int(cmd[1]))
            elif cmd[0] == "remove":
                if int(cmd[1]) in s:
                    s.remove(int(cmd[1]))
            elif cmd[0] == "check":
                if int(cmd[1]) in s:
                    print(1)
                else:
                    print(0)
            elif cmd[0] == "toggle":
                if int(cmd[1]) in s:
                    s.remove(int(cmd[1]))
                else:
                    s.add(int(cmd[1]))
            elif cmd[0] == "all":
                s = {i for i in range(1,21)}
            elif cmd[0] == "empty":
                s.clear()

if __name__ == "__main__":
    s = Solution()
    s.generate()