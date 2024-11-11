from collections import Counter
import heapq

class Solution:
    def result(self, nums:list, k:int) -> list:
        freq = Counter(nums)
        h = []
        for item in freq:
            heapq.heappush(h,(-freq[item], item))
        res=[]
        for _ in range(k):
            res.append(heapq.heappop(h)[1])

        return res

class Solution_:
    def result(self, nums:list, k:int) -> list:
        return list(zip(*Counter(nums).most_common(k)))[0]

nums = [4,1,1,1,2,2,3]
k = 2
# print(*nums) # *은 시퀀스 언패킹 연산자
print(Solution_.result(Solution_, nums, k))

# ** 활용 예제
date = {'year':2020, 'month':11, 'day':10}
res = {**date, 'year':2024, 'day':11}
print(res)