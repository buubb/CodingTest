import sys
import heapq
input = sys.stdin.readline

class Solution:
    def largestElement(self, arr, k):
        l = len(arr)
        for i in range(l):
            if i == l-k:
                print(heapq.heappop(arr))
                break
            heapq.heappop(arr)

    def findKthLargest(self, nums:list, k:int):
        heapq.heapify(nums)
        print(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)
    
    def findKthLargest_(self, nums:list, k:int):
        return heapq.nlargest(k, nums)[-1] # n번째 큰 수까지 리스트로 반환 -> 인덱스 -1 위치가 n번째 큰 수
    
    def findKthLargest_2(self, nums:list, k:int): # '정렬' 방식이 가장 빠르다.
        nums.sort()
        return nums[-k]

if __name__ == "__main__":
    s = Solution()
    arr = [3,2,3,1,2,4,5,5,6]
    print(s.findKthLargest_2(arr, 4))
    # s.largestElement(arr, 4)
    