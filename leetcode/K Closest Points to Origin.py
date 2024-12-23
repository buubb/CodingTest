import math
import heapq
class Solution:
    def kClosest(self, points:list, k:int) -> list:
        heap = []
        for (x,y) in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (dist, x, y))
        
        result = []
        for _ in range(k):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x,y))
        return result
    
if __name__ == "__main__":
    s = Solution()
    res = s.kClosest([[1,3], [-2,2]], 1)
    print(res)
