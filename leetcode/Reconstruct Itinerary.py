from collections import defaultdict
class Solution:
    def findItinerary(self):
        plan = [["ATL", "SFO"], ["JFK", "SFO"], ["JFK", "ATL"], ["SFO","ATL"], ["ATL", "JFK"]]
        dic = defaultdict(list)
        for item in sorted(plan, reverse=True):
            dic[item[0]] += [item[1]]
        
        result = []
        def dfs(now):
            result.append(now)
            if not dic[now]:
                return
            while dic[now]:
                dfs(dic[now].pop())
        dfs("JFK")
        return result

s = Solution()
print(s.findItinerary())
