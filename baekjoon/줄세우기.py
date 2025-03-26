import sys
input = sys.stdin.readline

class Solution:
    def answer(self):
        T = int(input())
        for _ in range(T):
            arr = list(map(int, input().split()))
            
            current = 2
            cnt = 0
            stack = [arr[1]]
            while current <= 20:
                for i in range(len(stack)):
                    # 앞 사람 중 현재보다 큰 사람이 있는 경우
                    if stack[i] > arr[current]:
                        cnt += len(stack) - i
                        stack.insert(i, arr[current])
                        current += 1
                        break
                else:
                    # 앞 사람들보다 키가 큰 경우
                    stack.append(arr[current])
                    current += 1
            print(arr[0], cnt)


if __name__ == "__main__":
    s = Solution()
    s.answer()