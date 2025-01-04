import heapq
class Solution:
    def reconstructQueue(self, q:list):
        hq = []
        for person in q:
            heapq.heappush(hq, (-person[0], person[1]))
        
        result = []
        while hq:
            person = heapq.heappop(hq)
            result.insert(person[1], (-person[0],person[1])) # person[1]을 인덱스로 활용용
        print(result)

if __name__ == "__main__":
    s = Solution()
    arr = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    s.reconstructQueue(arr)