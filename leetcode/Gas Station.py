class Solution:
    def canCompleteCircuit(self, gas:list, cost:list):
        for start in range(len(gas)):
            fuel = 0
            isOk = True
            for i in range(start, len(gas)+start):
                i = i % len(gas)
                if fuel + gas[i] < cost[i]:
                    isOk = False
                    break
                else:
                    fuel += gas[i] - cost[i]
            if isOk:
                print(start)
                return
        print(-1)
    
    def canCompleteCircuit2(self, gas:list, cost:list):
        # 모든 주유소 방문 가능 여부 판별별
        if sum(gas) < sum(cost):
            print(-1)
            return
        start, fuel = 0, 0
        for i in range(len(gas)):
            # 출발점이 안 되는 지점 판별
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        print(start)



if __name__ == "__main__":
    s = Solution()
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    s.canCompleteCircuit2(gas, cost)
