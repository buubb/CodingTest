import sys, heapq
input = sys.stdin.readline

class Solution:
    def num3(self):
        N = int(input())
        result = 0
        power = 0
        
        while N > 0:
            if N & 1:  # 현재 비트가 1인지 확인
                result += 3**power
            N >>= 1  # N을 오른쪽으로 1비트 쉬프트
            power += 1  # 거듭제곱 증가
        
        print(result)


if __name__ == "__main__":
    s = Solution()
    s.num3()