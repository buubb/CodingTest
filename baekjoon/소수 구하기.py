import sys
input = sys.stdin.readline

class Solution:
    def demical_(self):
        M, N = map(int, input().split())
        for i in range(M, N+1):
            isPrime = True
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    isPrime = False
                    break
            if isPrime:
                print(i)

    def demical_a(self):
        M, N = map(int, input().split())

        # 범위 2부터 N까지의 소수 여부를 저장할 배열
        is_prime = [True] * (N + 1)
        is_prime[0], is_prime[1] = False, False  # 0과 1은 소수가 아님

        # 에라토스테네스의 체
        for i in range(2, int(N**0.5) + 1):
            if is_prime[i]:  # 소수라면
                for j in range(i * i, N + 1, i):  # i의 배수들을 제거
                    is_prime[j] = False

        # 범위 M에서 N까지의 소수 출력
        for i in range(M, N + 1):
            if is_prime[i]:
                print(i)

if __name__ == "__main__":
    s = Solution()
    s.demical_a()