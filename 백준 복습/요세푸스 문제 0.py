import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    # 비효율적인 방법,, (224ms) 큐를 사용하라고
    def wrong_answer(self): 
        n, k = map(int, input().split())
        arr = [i for i in range(1, n+1)]
        check = [False] * (n)
        res = [str(arr[k-1])]
        check[k-1] = True
        cnt, idx = 0, k-1
        while True:
            for i in range(n):
                if not check[i]:
                    break
            else:
                break
                
            while cnt < k:
                idx = (idx + 1) % n
                if not check[idx]:
                    cnt += 1

            if not check[idx]:
                res.append(str(arr[idx]))
                check[idx] = True
                cnt = 0

        print("<"+ ', '.join(res) + ">")
    
    # 68ms
    def answer(self):
        n, k = map(int, input().split())
        Q = deque(map(str, range(1, n+1)))
        res = []
        while Q:
            for _ in range(k-1):
                Q.append(Q.popleft())
            res.append(Q.popleft())
        
        print("<"+ ', '.join(res) + ">")


if __name__ == "__main__":
    s = Solution()
    s.answer()