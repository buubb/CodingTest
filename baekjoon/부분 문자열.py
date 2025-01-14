import sys
input = sys.stdin.readline

class Solution:
    def substring(self):
        while True:
            line = input().strip()
            if not line:  # 입력이 더 이상 없으면 종료
                break
            s, t = line.split()
            isSubstring = True
            k = 0
            for sw in s:
                find = False
                for i in range(k, len(t)):
                    if sw == t[i]:
                        find = True
                        k = i + 1
                        break
                if not find:  # 문자를 찾을 수 없으면 False
                    isSubstring = False
                    break
            if isSubstring:
                print("Yes")
            else:
                print("No")

if __name__ == "__main__":
    s = Solution()
    s.substring()
